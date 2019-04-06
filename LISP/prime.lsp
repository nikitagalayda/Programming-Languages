(DEFUN prime(num)
	(if (<= num 2)
 		(return-from prime 1))
 	(if (= (rem num 2) 0)
 		(return-from prime 0))
	(loop for i from 3 to (- num 1)
		do (if (= (rem num i) 0)
			(return-from prime 0)
		)
	)
	1
)
;(print (prime 107))


