model lab8
  parameter Real N = 1, R = 1, K = 5.3, C = 1;
  Real W(start = 0.1), Q(start = 1);
equation
  der(W) = 1/R - (W*delay(W, R)*K*delay(Q, R))/(2*R);
  if (Q == 0) then
    der(Q) = max(N*W/R - C, 0);
  else
    der(Q) = N*W/R - C;
  end if;
  annotation(
    experiment(StartTime = 0, StopTime = 100, Tolerance = 1e-06, Interval = 0.2));
end lab8;