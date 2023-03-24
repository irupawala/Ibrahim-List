package com.google;

import java.util.Objects;

public class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }


        @Override
    public boolean equals(Object obj) { // notice here we cannot change the passed parameter of object type because then signature will defer and it won't be overwritten
        if (this == obj) // checking if object is compared to itself
            return true;

        if (!(obj instanceof Point)) return false; // As discussed in the earlier section we need to make sure that the object is of point type or else an exception will be raised during runtime

        var other = (Point) obj; // downcasting the object to point type as the object we will be receiving will be of point type
        return (this.x == x && this.y == y);
    }

   // As a best practice whenever we overwrite the equals method we should also overwrite hashCode method


    @Override
    public int hashCode() {
        //return super.hashCode(); It is calling hashcode() based on the implementation in the base class but instead what we want is to generate hashcode based on the value of this field x and y
        // To generate hashcode we will use class "Objects" and method in it called hash.
        // We can give this method bunch of values and it will generate a hash value.
        // A hash value in theory uniquely identifies objects.
        // one or more arguments can be given to hash method
        return Objects.hash(x,y);

    }

}
