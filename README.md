## django-profile-middleware
An easy to use customizable django profiling middleware for Django VERSION below 1.10. 
(For version 1.10 or above refer [here](https://github.com/someshchaturvedi/customizable-django-profiler))

## Requirement
Django VERSION below 1.10 and python 3.x

## Installation

```$ pip install django-profile-middleware```

## Middleware

 **Motivation:** To provide an easy to use cProfile middleware to find bottlenecks in code.            

**How To Use**
(after installation)

In your settings add:

```django_profile_middleware.middleware.ProfilerMiddleware``` to the end your ```MIDDLEWARE_CLASSES``` and 
```django_profile_middleware``` to your ```INSTALLED_APPS```
 
```In case you also want to profile any of your custom middleware, just add all those middlewares below this one```.


For example:

```bash
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ....

    'django_profile_middleware.middleware.ProfilerMiddleware',

]

INSTALLED_APPS = [
    ....
    'django_profile_middleware',
    ....
] 
```
### Enable
Add ```PROFILER``` in project's ```settings.py``` and set ```enable = True```.
Also make sure project running in DEBUG mode ```DEBUG = True```

```bash
DEBUG = True

PROFILER = {
    'enable': True,
}

```
And 

Profiling results will be printed on the console and will also be saved in a ```profiling_results.txt``` file.
```profiling_results.txt``` file will be created if not present and updated with the results at end if a file with same name already exists.

Example

```bash
        197 function calls (192 primitive calls) in 0.002 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   ...      ...      ...       ...     ...           ...
   ...      ...      ...       ...     ...           ...

```

## Customize

You can customize the Profiler settings via adding optional fields to ```PROFILER``` key in ```settings.py```

Default are

```bash
PROFILER = {
    'enable': True,

    #optional fields
    'sort': 'time',
    'count': None ,
    'output': ['console','file'],             
    'file_location': 'profiling_results.txt'

}
```

## Description of optional fields
### enable
Set this key to ```True``` to enable Profiler

```bash
'enable': True
```
To disable set to ```False```
```bash
'enable': False
```

### sort
Sort according to the set value. Default is ```'time'```.
See [documentaion](http://docs.python.org/2/library/profile.html#pstats.Stats.sort_stats) for more options

### count
Specify number of rows to output. By Default it will give all the rows.

### output
Specify the form of output. Default is ```['console',"file"]```. In case only one of them is required just mention that in ou2tput field
```'file'``` will write the file specified by ```'file_location'``` field.


```bash
'output': ['console', 'file']  # default value
```
```bash
'output': ['console']
```


### file_location
Specify the location of file you want to write in the results. **Only valid if ```'file'``` in ```'output'``` field**. Default value ```profiling_results.txt```





## Decorator

I have also added a decorator in the package which can be used optionally according to one's requirement.

**Motivation:** In case API takes very less time say 10 ms to execute, it is difficult to know which function is taking the maximum time, as, even the slowest one may take just 1 ms or even less . 
So this decorator provides you an option to run the whole code multiple times and thus scaling the total time to a more indicative value.

**How To Use**
(after installation)
In your views.py file add :

```
from django_profile_middleware.decorator import iterator
```

and at the function you want to run multiple time add decorator:
```
@iterator( *no. of times you want it to run )
```
for example:
```
@iterator(100)
```

## Author

* **Himanshu Goyal**

Email me with any questions: [hggoyal06@gmail.com](hggoyal06@gmail.com).

