# Notes
Implementation of the Citrine challenge.  
Superscripts aren't available in the response, instead m<sup>2</sup> is available as `m2` and m<sup>3</sup> is available as `m3`. Response are of mimetime `application/json`, as specified, and follow the format:

```
{  
    'unit_name': <string of units>,   
    'multiplication_factor': <numerical conversion factor formatted to 14 decimal places>  
}
```

No explicit handling of numerics is implemented; if a number becomes too large or too small, it will handle the number as python would handle it.

Input is assumed to be non-SI units, and is case-sensitive.

# Implementation
- python (2.7.12)
- flask

# Installation
```
    pip install virtualenv
    virtualenv new citrine
    pip install -r requirements.txt
```

# Server 
To run the server in development mode, the command is as simple as: `./run.sh`