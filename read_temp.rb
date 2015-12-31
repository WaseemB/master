#!/usr/bin/env ruby
#  Purpose:
#    Script to read temperature probe
#
#  References:
#    None
#
#  Details:
#    Input: device <device>
#    Dependent on yml file raspberrypi.yml which should be located in eswradio home dir (/home/eswradio).
#
#  ------------------------ Copyright ERICSSON AB 2012 ------------------------
#  The programs may be used and/or copied only with the written permission from
#  ERICSSON AB or in accordance with the terms and conditions stipulated in
#  the agreement/contract under which the programs have been supplied.

require 'yaml'

@conf_file = '/home/pi/my_prog/raspberrypi.yml'
#@conf_file = 'temp_sensors.yaml'

def init
   unless ARGV.length == 1
      puts "Usage: #{$0} <device>" 
      exit -1
   end
   @device_id = ARGV[0].to_i
   @conf = YAML.load_file @conf_file
   devices = []
   @conf['TEMP_SENSORS'].each_key{|key| devices.push key}
   unless devices.include? @device_id
      puts "Unsupported device, #{@device_id}. (#{devices})"
      exit -1
   end
end

def get_device_path(device_id = 0)
   base_dir = @conf['BASE_DIR']
   sensors = @conf['TEMP_SENSORS']

   device_folder = base_dir + sensors[device_id]['serial']
   unless Dir.exist? device_folder
      puts "Temp sensor #{device_folder} not found!"
      exit -1
   end
   device_file = "#{device_folder}/w1_slave"
end

def read_temp(file)
  lines = File.readlines(file)
  while lines[0].strip[-3..-1] != "YES" do
    lines = File.readlines(file)
  end
  
  equals_pos = lines[1].index("t=")
  if equals_pos > -1
    temp_string = lines[1][equals_pos+2..-1]
    temp_c = temp_string.to_f / 1000.0
    
    return "#{temp_c}\n"
  end
  
  return ""
end

def main
  init
  device_file = get_device_path(@device_id)
  
  temp = read_temp(device_file)
  puts temp
end
main

