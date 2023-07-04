package com.test.smart_planter_android.data_model

import android.content.Context
import android.content.Context.MODE_PRIVATE
import android.content.SharedPreferences
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase

class DataSend(context : Context){
    private val db = Firebase.firestore
    private var spf : SharedPreferences = context.getSharedPreferences("emName", MODE_PRIVATE)

    fun setLedOnOFF(str : String){
        val led = hashMapOf(
            "LED" to str
        )

        db.collection(spf.getString("eName","default")!!).document("LED").set(led)
    }

    fun setLedR(R : String){
        val ledR = hashMapOf(
            "R" to R
        )

        db.collection(spf.getString("eName","default")!!).document("LED_R").set(ledR)
    }

    fun setLedG(G : String){
        val ledG = hashMapOf(
            "G" to G
        )

        db.collection(spf.getString("eName","default")!!).document("LED_G").set(ledG)
    }

    fun setLedB(B : String){
        val ledB = hashMapOf(
            "B" to B
        )

        db.collection(spf.getString("eName","default")!!).document("LED_B").set(ledB)
    }


    fun setTime(time : HashMap<String,Long>){
        db.collection(spf.getString("eName","default")!!).document("Time").set(time)
    }

}