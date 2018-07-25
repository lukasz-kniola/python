%macro msha_hash(id, key, keylen);
  %let keyx1 = %substr(%sysfunc(sha256(%cmpres(%sysfunc(reverse(&key)))), $hex64.),1,4);

  %let s=0;
  %do i =1 %to %length(&key);
    %let s = %eval(&s+%sysfunc(rank(%substr(&key,&i,1))));
  %end;
  %let start = %sysfunc(mod(&s,64));
  %let asc = %sysfunc(byte(%eval(33+%sysfunc(mod(&s,93)))));
  %let ascn = %sysfunc(mod(&s,13));
  %let keyx2 = %sysfunc(repeat(%str(&asc),&ascn-1));

  %let sha=%sysfunc(repeat(%sysfunc(sha256(%str(13&keyx1.&id.&keyx2.&key)), $hex64.),1));
  %let hash = %substr(&sha,%eval(&start+1),&keylen);
  &hash;

%mend msha_hash;

%let h = %msha_hash(101-001, 4klfgh6*, 12);
%put &h;


%macro sha_hash(id, key, keylen);
  _X_keyx1 = substr(put(sha256(compress(reverse(&key))), $hex64.),1,4);
  _X_s=0;
  do _X_i =1 to length(&key);
    _X_s = _X_s+rank(substr(&key,_X_i,1));
  end;
  _X_start=mod(_X_s,64);
  _X_asc = byte(33 + mod(_X_s,93));
  _X_ascn = mod(_X_s,13);
  _X_sha=repeat(put(sha256('13'||compress(_X_keyx1)||compress(&id)||repeat(_X_asc,_X_ascn-1)||compress(&key)), $hex64.),1);
  hash = substr(_X_sha,_X_start+1,&keylen);
  drop _X_:;
%mend sha_hash;

data a;
  do i=1 to 20;
    subjid = '101-'||put(i,z3.);
    %sha_hash(subjid, "4klfgh6*", 12);
    output;
  end;
run;
