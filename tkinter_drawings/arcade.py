ó
Z^c           @   s»   d  Z  d d l Z d d l Z d d l Z d d l Z d Z d Z d Z d Z d Z	 d Z
 d Z d Z d	 e j f d
     YZ d e j f d     YZ d   Z e d k r· e   n  d S(   sv  
Sprite Follow Player 2

This calculates a 'vector' towards the player and randomly updates it based
on the player's location. This is a bit more complex, but more interesting
way of following the player.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_follow_simple_2
iÿÿÿÿNg      à?gÉ?i   i   iX  s%   Sprite Follow Player Simple Example 2t   Coinc           B   s   e  Z d  Z d   Z RS(   sx   
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    c   	      C   s¶   |  j  |  j 7_  |  j |  j 7_ t j d  d k r² |  j  } |  j } | j  } | j } | | } | | } t j | |  } t j |  t	 |  _ t j
 |  t	 |  _ n  d S(   s<  
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        id   i    N(   t   center_xt   change_xt   center_yt   change_yt   randomt	   randranget   matht   atan2t   cost
   COIN_SPEEDt   sin(	   t   selft   player_spritet   start_xt   start_yt   dest_xt   dest_yt   x_difft   y_difft   angle(    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyt   follow_sprite&   s    
				

(   t   __name__t
   __module__t   __doc__R   (    (    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyR        s   t   MyGamec           B   s;   e  Z d  Z d   Z d   Z d   Z d   Z d   Z RS(   s    Our custom Window Classc         C   s   t    j t t t  t j j t j j t	   } t j
 |  d |  _ d |  _ d |  _ d |  _ |  j t  t j t j j  d S(   s    Initializer i    N(   t   supert   __init__t   SCREEN_WIDTHt   SCREEN_HEIGHTt   SCREEN_TITLEt   ost   patht   dirnamet   abspatht   __file__t   chdirt   Nonet   player_listt	   coin_listR   t   scoret   set_mouse_visiblet   Falset   arcadet   set_background_colort   colort   AMAZON(   R   t	   file_path(    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyR   M   s    				c         C   sÅ   t  j   |  _ t  j   |  _ d |  _ t  j d t  |  _ d |  j _ d |  j _	 |  j j
 |  j  xW t t  D]I } t d t  } t j t  | _ t j t  | _	 |  j j
 |  qt Wd S(   s/    Set up the game and initialize the variables. i    sI   :resources:images/animated_characters/female_person/femalePerson_idle.pngi2   s$   :resources:images/items/coinGold.pngN(   R+   t
   SpriteListR&   R'   R(   t   Spritet   SPRITE_SCALING_PLAYERR   R   R   t   appendt   ranget
   COIN_COUNTR    t   SPRITE_SCALING_COINR   R   R   R   (   R   t   it   coin(    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyt   setupf   s    	c         C   sY   t  j   |  j j   |  j j   d j |  j  } t  j | d d t  j j	 d  d S(   s    Draw everything s	   Score: {}i
   i   i   N(
   R+   t   start_renderR'   t   drawR&   t   formatR(   t	   draw_textR-   t   WHITE(   R   t   output(    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyt   on_draw   s
    
c         C   s   | |  j  _ | |  j  _ d S(   s    Handle Mouse Motion N(   R   R   R   (   R   t   xt   yt   dxt   dy(    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyt   on_mouse_motion   s    c         C   sj   x! |  j  D] } | j |  j  q
 Wt j |  j |  j   } x' | D] } | j   |  j d 7_ qC Wd S(   s    Movement and game logic i   N(   R'   R   R   R+   t   check_for_collision_with_listt   killR(   (   R   t
   delta_timeR8   t   hit_list(    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyt	   on_update   s    
(   R   R   R   R   R9   R@   RE   RJ   (    (    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyR   J   s   			
	c          C   s!   t    }  |  j   t j   d S(   s    Main method N(   R   R9   R+   t   run(   t   window(    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyt   main¤   s    	
t   __main__(   R   R   R+   R   R   R2   R6   R5   R
   R   R   R   t   SPRITE_SPEEDR1   R    t   WindowR   RM   R   (    (    (    sK   /home/tony/Desktop/My_repos/xgboost-with-raymond/tkinter_drawings/arcade.pyt   <module>   s"   *Z	