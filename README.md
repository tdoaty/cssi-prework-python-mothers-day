## Python Mother's Day!

<img src = "http://forthemommas.com/wp-content/uploads/2015/05/hallmark.jpg">

### Intro

Mother's day is coming up, and you've been hired by Hallmark to develop some e-cards! We're going to write some methods to wish people Happy Mother's Day for us. You'll be coding your solutions in `mothers_day.py`.

#### Step 1 - a method with no arguments

Define a method, `mothers_day`, that returns a string that says `"Happy Mother's Day, Mom!"`

#### Step 2 - a method with arguments

Your mothers day method is great, but it can only wish a Happy Mother's Day to Mom! Some of your customers want to wish a Happy Mother's Day to their grandmothers, sisters, and friends. Create a new method called `better_mothers_day` so that it takes in a name and returns a personalized greeting. For example, calling `better_mothers_day("Beyonce")` should return `"Happy Mother's Day, Beyonce!"`

#### Step 3 - a method with default arguments

Your new method is great, but sometimes we need to send a quick card and can't write in the whole name. We need to be able to send a card quickly with no arguments or the same card with a name. Create a function `even_better_mothers_day()` that has a default value. Calling `even_better_mothers_day()` returns `"Happy Mother's Day, Mom!"` and ``even_better_mothers_day("Beyonce")` returns `"Happy Mother's Day, Beyonce!"`

### Step 4 - multiple arguments and more

Our method now works great for mother's day, but we want to let users customize it even more. Create a new function, `holiday_greeting()` that takes in a to, from, and a holiday and returns a personalized greeting. For example, calling `holiday_greeting("Beyonce", "Jay-Z", "Fourth of July")` should return `"Happy Fourth of July, Beyonce! - From Jay-Z"`. If no arguments are specified, the method should return `"Happy Mother's Day, Mom! - From Your Favorite Child"`

### Bonus

+ Create a file in this directory called `holiday_greeting.py`. First build out a command line user interface. It should:
	+ Welcome the user to your program
	+ Take in their to, from, and holiday inputs and store them in variables. 
	+ Run your method and show the user your results!

