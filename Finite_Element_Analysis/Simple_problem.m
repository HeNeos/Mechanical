format long
A = [];
K = [];
NodesCondition = [];
ForcesCondition = [];

function [nU,NodesCondition] = UBoundaryCondition(nU,u,i,NodesCondition)
  NodesCondition = [NodesCondition i];
  nU(i,1) = u;
endfunction

function [nF,ForcesCondition] = FBoundaryCondition(nF,f,i,ForcesCondition)
  nF(i,1) = f;
  ForcesCondition = [ForcesCondition i];
endfunction

function nS = AssemblyStiffness(nS, k, i)
  j = i+1;
  nS(i,i) += k;
  nS(i,j) -= k;
  nS(j,i) -= k;
  nS(j,j) += k;
endfunction

function nS = Initialize(nS,nU,nF, K)
  Nodes = size(nU)(1);
  for i = 1:Nodes
    nU(i,1) = -1;
    nF(i,1) = -1;
  endfor
  for i = 1:Nodes-1
    a = AssemblyStiffness(nS,K(i),i);
    nS = a;
  endfor
endfunction

function newS = PreSolvingS(S,NodesCondition)
  Nodes = size(S)(1);
  nsize = Nodes-size(NodesCondition)(1);
  newS = zeros(nsize,nsize);
  contr = 0;
  for i=1:Nodes
    contc = 0;
    flagr = 0;
    for k=1:size(NodesCondition)(1)
      if i==NodesCondition
        flagr = 1;
        break
      endif
    endfor
    if flagr == 1
      continue
    endif
    contr += 1;
    for j=1:Nodes
      flagc = 0;
      for k=1:size(NodesCondition)(1)
        if j==NodesCondition(k)
          flagc = 1;
          break
        endif
      endfor
      if flagc == 1
        continue
      endif
      contc += 1;
      newS(contr,contc) = S(i,j);
    endfor
  endfor
endfunction

function newF = PreSolvingF(nF,nS,nU,NodesCondition)
  Nodes = size(nF)(1);
  nsize = Nodes-size(NodesCondition)(1);
  newF = zeros(nsize,1);
  contr = 0;
  for i=1:Nodes
    flagr = 0;
    for k=1:NodesCondition
      if(i == NodesCondition(k))
        flagr = 1;
        break
      endif
    endfor
    if flagr == 1
      for k=1:Nodes
        nF(k,1) = nF(k,1) - nS(k,1)*nU(i,1);
      endfor
      continue
    endif
  endfor
    for i=1:Nodes
      flagr = 0;
      for k=1:size(NodesCondition)(1)
        if i==NodesCondition(k)
          flagr = 1;
          break
        endif
      endfor
      if flagr == 1
        continue
      endif
      contr += 1;
      newF(contr,1) = nF(i,1);
    endfor
endfunction

function [nU, nF] = Solve(nS, nU, nF, NodesCondition)
  Nodes = size(nS)(1);
  newS = PreSolvingS(nS,NodesCondition);
  newF = PreSolvingF(nF,nS,nU,NodesCondition);
  u = newS\newF;
  contr = 0;
  for i=1:Nodes
    flagr = 0;
    for k=1:size(NodesCondition)(1)
      if i == NodesCondition(k)
        flagr = 1;
        break
      endif
    endfor
    if flagr == 1
      continue
    endif
    contr += 1;
    nU(i,1) = u(contr,1);
  endfor
  nF = nS*nU;
endfunction



Nodes = 100;
Nodes = 2*Nodes+1;
E = 2e5;
L = 1500;
b0 = 1000;
bf = 0;
e = 120;
P = 5e4;
y = 0.0764532e-3;

dL = L/(Nodes-1);
for i=1:Nodes
  b = b0-(i-1)*((b0-bf)/(Nodes-1));
  nb = b0-(i)*(b0-bf)/(Nodes-1);
  b = ((b+nb)*e)/2;
  A = [A b];
endfor


for i=1:Nodes-1
  K = [K E*A(i)/dL];
endfor


NumberOfElement = Nodes-1;
StiffnessMatrix = zeros(Nodes,Nodes);
U = zeros(Nodes,1);
F = zeros(Nodes,1);
StiffnessMatrix = Initialize(StiffnessMatrix,U,F,K);
[U,NodesCondition] = UBoundaryCondition(U,0,1,NodesCondition);

for i=2:Nodes
  if(mod(i,2) == 0)
    W = y*(A(i-1)+A(i))*dL;
    [F,ForcesCondition] = FBoundaryCondition(F,W,i,ForcesCondition);
  else
    [F,ForcesCondition] = FBoundaryCondition(F,0,i,ForcesCondition);
  endif
endfor

if(mod(NumberOfElement/2,2) == 1)
  W = y*(A(NumberOfElement/2)+A(NumberOfElement/2-1))*dL;
  [F,ForcesCondition] = FBoundaryCondition(F,W+P,NumberOfElement/2+1,ForcesCondition);
  else
  [F,ForcesCondition] = FBoundaryCondition(F,P,NumberOfElement/2+1,ForcesCondition);
endif

[U, F] = Solve(StiffnessMatrix, U, F, NodesCondition);

disp("Stiffness Matrix")
disp(StiffnessMatrix)
disp("Displacements")
disp(U)
disp("Forces")
disp(F)


