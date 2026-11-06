% Alternatywne rozwiązanie tego samego układu w GNU Octave.
A = [2 1; 1 3];
b = [5; 5];
v = A \ b;

fid = fopen("octave_results.txt", "w");
if (fid < 0)
  error("Nie można otworzyć pliku wynikowego");
endif
fprintf(fid, "x=%.6f\n", v(1));
fprintf(fid, "y=%.6f\n", v(2));
fclose(fid);
disp(v);
