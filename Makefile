.PHONY: *

new:
	cp -r template day$(day) && \
	echo "" >> Makefile && \
	echo "day$(day):" >> Makefile && \
	printf "\tcd ./day$(day) && python solution.py $$\{test}\n" | sed 's/\\{/{/g' >> Makefile

day1:
	cd day1 && python day1.py

day2: 
	cd ./day2 && python day2.py 

day3: 
	cd ./day3 && python day3.py 

day4: 
	cd ./day4 && python day4.py 
	
day5: 
	cd ./day5 && python solution.py 

day6: 
	cd ./day6 && python solution.py 

day7: 
	cd ./day7 && python solution.py 

day8:
	cd ./day8 && python solution.py ${test}
