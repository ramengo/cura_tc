	        nozzle			
	        0,6	        0,8	        1	        1,2
fine	    0,15			
standard	0,3	        0,3		
draft	    0,45	    0,45	    0,45	
superdraft		        0,6	        0,6	         0,6
fast			                    0,75	     0,75
ultrafast				                         0,9


{speed_print}				Print Speed	The speed at which printing happens.
{speed_infill}				Infill Speed	The speed at which infill is printed.
{speed_wall}				Wall Speed	The speed at which the walls are printed.
{speed_wall_0}				Outer Wall Speed	The speed at which the outermost walls are printed. Printing the outer wall at a lower speed improves the final skin quality. However, having a large difference between the inner wall speed and the outer wall speed will affect quality in a negative way.
{speed_wall_x}				Inner Wall Speed	The speed at which all inner walls are printed. Printing the inner wall faster than the outer wall will reduce printing time. It works well to set this in between the outer wall speed and the infill speed.
{speed_wall_0_roofing}		Top Surface Outer Wall Speed	The speed at which the top surface outermost wall is printed.
{speed_wall_x_roofing}		Top Surface Inner Wall Speed	The speed at which the top surface inner walls are printed.
{speed_roofing}				Top Surface Skin Speed	The speed at which top surface skin layers are printed.
{speed_topbottom}			Top/Bottom Speed	The speed at which top/bottom layers are printed.
{speed_support}				Support Speed	The speed at which the support structure is printed. Printing support at higher speeds can greatly reduce printing time. The surface quality of the support structure is not important since it is removed after printing.
{speed_support_infill}		Support Infill Speed	The speed at which the infill of support is printed. Printing the infill at lower speeds improves stability.
{speed_support_interface}	Support Interface Speed	The speed at which the roofs and floors of support are printed. Printing them at lower speeds can improve overhang quality.
{speed_support_roof}		Support Roof Speed	The speed at which the roofs of support are printed. Printing them at lower speeds can improve overhang quality.
{speed_support_bottom}		Support Floor Speed	The speed at which the floor of support is printed. Printing it at lower speed can improve adhesion of support on top of your model.
{speed_prime_tower}			Prime Tower Speed	The speed at which the prime tower is printed. Printing the prime tower slower can make it more stable when the adhesion between the different filaments is suboptimal.
{speed_travel}				Travel Speed	The speed at which travel moves are made.
{speed_layer_0}				Initial Layer Speed	The speed for the initial layer. A lower value is advised to improve adhesion to the build plate. Does not affect the build plate adhesion structures themselves, like brim and raft.
{speed_print_layer_0}		Initial Layer Print Speed	The speed of printing for the initial layer. A lower value is advised to improve adhesion to the build plate.
{speed_travel_layer_0}		Initial Layer Travel Speed	The speed of travel moves in the initial layer. A lower value is advised to prevent pulling previously printed parts away from the build plate. The value of this setting can automatically be calculated from the ratio between the Travel Speed and the Print Speed.
{skirt_brim_speed}			Skirt/Brim Speed	The speed at which the skirt and brim are printed. Normally this is done at the initial layer speed, but sometimes you might want to print the skirt or brim at a different speed.
{speed_z_hop}


speed_print = =math.ceil(speed_print * 100 / 100)
speed_infill = =math.ceil(speed_print * 100 / 100) 
speed_wall = =math.ceil(speed_print * 60 / 100) 
speed_wall_0 = =math.ceil(speed_print * 60 / 100) 
speed_wall_x = =math.ceil(speed_print * 80 / 100) 
speed_wall_0_roofing = =math.ceil(speed_print * 60 / 100) 
speed_wall_x_roofing = =math.ceil(speed_print * 60 / 100) 
speed_roofing = =math.ceil(speed_print * 50 / 100) 
speed_topbottom = =math.ceil(speed_print * 50 / 100) 
speed_support = =math.ceil(speed_print * 70 / 100) 
speed_support_infill = =math.ceil(speed_print * 70 / 100) 
speed_support_interface = =math.ceil(speed_print * 60 / 100) 
speed_support_roof = =math.ceil(speed_print * 60 / 100) 
speed_support_bottom = =math.ceil(speed_print * 60 / 100) 
speed_prime_tower = =math.ceil(speed_print * 50 / 100) 
speed_travel = 300 
speed_layer_0 = 25
speed_print_layer_0 = 25
speed_travel_layer_0 = =math.ceil(speed_travel * 50 / 100) 
skirt_brim_speed = 25
speed_z_hop = 5



quality/fabbrix/elemento_tc/elemento_tc_{0.6,0.8,1.0,1.2}_CFF_{fine,standard,draft,superdraft,fast,ultrafast}.inst.cfg

setting_version\s*=\s*\d+
