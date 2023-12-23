from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def time(request):
  return render(request, 'time.html')

def cartesian(request):
  return render(request, 'cartesian.html')

def coordinate(request):
  return render(request, 'coordinate.html')

from math import cos, sin, radians

import math

def xyz2blh(x, y, z, precision):
    a = 6378137.0  
    b = 6356752.3141  

    e_squared = 1 - (b**2 / a**2)
    p = math.sqrt(x**2 + y**2)


    lat = math.atan2(z, p * (1 - e_squared))
    lon = math.atan2(y, x)
    N = a / math.sqrt(1 - e_squared * math.sin(lat)**2)
    alt = p / math.cos(lat) - N

    while True:
        prev_lat = lat
        prev_N = N
        prev_alt = alt

        lat = math.atan2(z, p * (1 - e_squared * (N / (N + alt))))
        N = a / math.sqrt(1 - e_squared * math.sin(lat)**2)
        alt = p / math.cos(lat) - N

        if abs(alt - prev_alt) < precision:
            break

    lat = math.degrees(lat)
    lon = math.degrees(lon)

    return lat, lon, alt




def rotate_3d(coordinates, angle_x, angle_y, angle_z):
    ang_x_rad, ang_y_rad, ang_z_rad = radians(angle_x), radians(angle_y), radians(angle_z)
    
    def rotate_x(coord):
        return [
            coord[0],
            coord[1] * cos(ang_x_rad) - coord[2] * sin(ang_x_rad),
            coord[1] * sin(ang_x_rad) + coord[2] * cos(ang_x_rad)
        ]

    def rotate_y(coord):
        return [
            coord[0] * cos(ang_y_rad) + coord[2] * sin(ang_y_rad),
            coord[1],
            -coord[0] * sin(ang_y_rad) + coord[2] * cos(ang_y_rad)
        ]

    def rotate_z(coord):
        return [
            coord[0] * cos(ang_z_rad) - coord[1] * sin(ang_z_rad),
            coord[0] * sin(ang_z_rad) + coord[1] * cos(ang_z_rad),
            coord[2]
        ]

    coordinates = rotate_x(coordinates)
    coordinates = rotate_y(coordinates)
    coordinates = rotate_z(coordinates)

    return coordinates



def convert_time_to_different_scales(year, month, day, sec_of_day):
    leap_second_dates = [
        (1981, 6, 30), (1982, 6, 30), (1983, 6, 30), (1985, 6, 30),
        (1987, 12, 31), (1989, 12, 31), (1990, 12, 31), (1992, 6, 30),
        (1993, 6, 30), (1994, 6, 30), (1995, 12, 31), (1997, 6, 30),
        (1998, 12, 31), (2005, 12, 31), (2008, 12, 31), (2012, 6, 30),
        (2015, 6, 30), (2016, 12, 31), (2017, 12, 31), (2019, 12, 31),
        (2020, 12, 31), (2023, 6, 30)  
    ]

    leap_seconds = sum(1 for leap_date in leap_second_dates if (year, month, day) > leap_date)

    julian_date = 367 * year - (7 * (year + ((month + 9) // 12))) // 4 + (275 * month) // 9 + day + 1721013.5

    julian_date_with_frac = julian_date + (sec_of_day / 86400.0)

    leap_seconds_tai_utc = 10

    tai = (year, month, day, sec_of_day + leap_seconds_tai_utc + leap_seconds)
    utc = (year, month, day, sec_of_day + leap_seconds_tai_utc)
    tt = (year, month, day, sec_of_day + leap_seconds_tai_utc + leap_seconds)
    bdt = (year, month, day, sec_of_day - leap_seconds_tai_utc)  

    return tai, utc, tt, bdt, julian_date_with_frac

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def new_coordinate(request):
  if request.method == 'POST':
        data = json.loads(request.body)
        x = data.get('x', '0')
        y = data.get('y', '0')
        z = data.get('z', '0')
        rotx = data.get('rotx', '0')
        roty = data.get('roty', '0')
        rotz = data.get('rotz', '0')
        if x == 0:
            return JsonResponse({'error': 'Please write a cord'})
        else:
           old_coordinates = [int(x), int(y), int(z)]
           new_coordinates = rotate_3d(old_coordinates, int(rotx), int(roty), int(rotz))
           return JsonResponse({'result': f'New cordinates are: {new_coordinates}'})

  else:
     return JsonResponse({'error': 'Invalid request method'})

           
@csrf_exempt
def ellipsoid(request):
  if request.method == 'POST':
        data = json.loads(request.body)
        x = data.get('x', '0')
        y = data.get('y', '0')
        z = data.get('z', '0')
        precision = data.get('precision', '0')
        ellipsoid = data.get('ellipsoid', '0') 
        if x == 0:
            return JsonResponse({'error': 'Please write a cord'})
        else:
           phi, lam, h = xyz2blh(float(x), float(y), float(z),float(precision))
           return JsonResponse({'result': f'New cordinates are: {phi}, {lam},{h}'})





@csrf_exempt
def new_time(request):
  if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('datum', '0')
        sec = data.get('sec','0')
        if date == 0:
            return JsonResponse({'error': 'Please write a date'})
        else:
          result_date = date.split(".")
          year = int(result_date[2])
          month = int(result_date[1])
          day = int(result_date[0])
          sec_of_day = int(sec)
          tai_result, utc_result, tt_result, bdt_result ,julian_date_with_frac_result= convert_time_to_different_scales(year,month,day,sec_of_day)
          return JsonResponse({'result': f'TAI Time {tai_result}, UTC Time {utc_result}, TT Time  {tt_result}, BDT Time {bdt_result}, Julian Date {julian_date_with_frac_result}'})

  else:
     return JsonResponse({'error': 'Invalid request method'})











           
           
           




