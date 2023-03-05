package com.schneewittchen.rosandroid.widgets.button;

import com.schneewittchen.rosandroid.model.entities.widgets.BaseEntity;
import com.schneewittchen.rosandroid.model.repositories.rosRepo.node.BaseData;

import org.ros.internal.message.Message;
import org.ros.node.topic.Publisher;

import std_msgs.Int32;

/**
 * TODO: Description
 *
 * @author Dragos Circa
 * @version 1.0.0
 * @created on 02.11.2020
 * @updated on 18.11.2020
 * @modified by Nils Rottmann
 */

public class ButtonData extends BaseData {

    public boolean pressed;

    public  ButtonData(boolean pressed) {
        this.pressed = pressed;
    }

    @Override
    public Message toRosMessage(Publisher<Message> publisher, BaseEntity widget) {
        std_msgs.Int32 message = (Int32) publisher.newMessage();
        message.setData(1);
        return message;
    }
}
