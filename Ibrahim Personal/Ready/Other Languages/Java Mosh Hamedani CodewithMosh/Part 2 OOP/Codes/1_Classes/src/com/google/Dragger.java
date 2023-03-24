package com.google;

public class Dragger {
    public void drag (UIWidget draggable) { // here we are not creating an instance of the UIWidget class instead we are coupling our
        // Dragger class to UIWidget or Draggable Interface or contract
        // working with UIWidget interface here will give us more classes
    //public void drag (Draggable draggable) {
        draggable.drag();// This interface here is very lightweight as it has only one coupling point.
        System.out.println("Dragging Done !!");

    }
}
