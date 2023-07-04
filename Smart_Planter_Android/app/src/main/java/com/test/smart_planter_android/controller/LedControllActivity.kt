package com.test.smart_planter_android.controller

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.SeekBar
import android.widget.Toast
import com.test.smart_planter_android.R
import com.test.smart_planter_android.data_model.DataSend
import com.test.smart_planter_android.databinding.ActivityLedControllBinding

class LedControllActivity : AppCompatActivity() {
    private lateinit var binding : ActivityLedControllBinding
    private lateinit var dataModel : DataSend
    var ledButtonClicked = true

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLedControllBinding.inflate(layoutInflater)
        setContentView(binding.root)

        dataModel = DataSend(binding.root.context)

        binding.ledButtonController.setOnClickListener {
            when(ledButtonClicked){
                true -> { // 켜져있을때
                    ledButtonClicked = !ledButtonClicked
                    binding.ledButtonController.text = "OFF"
                    dataModel.setLedOnOFF("ON")
                    saveButtonState(true)
                }
                false ->{ // 꺼져있을때
                    ledButtonClicked = !ledButtonClicked
                    binding.ledButtonController.text = "ON"
                    dataModel.setLedOnOFF("OFF")
                    saveButtonState(false)
                }
            }
        }

        binding.RSeekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(p0: SeekBar?, p1: Int, p2: Boolean) {
                dataModel.setLedR(p1.toString())
            }

            override fun onStartTrackingTouch(p0: SeekBar?) {}

            override fun onStopTrackingTouch(p0: SeekBar?) {
                saveLedState("R",p0!!.progress)
            }

        })

        binding.GSeekBar2.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(p0: SeekBar?, p1: Int, p2: Boolean) {
                dataModel.setLedG(p1.toString())
            }

            override fun onStartTrackingTouch(p0: SeekBar?) {}

            override fun onStopTrackingTouch(p0: SeekBar?) {
                saveLedState("G",p0!!.progress)
            }

        })

        binding.BSeekBar3.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(p0: SeekBar?, p1: Int, p2: Boolean) {
                dataModel.setLedB(p1.toString())
            }

            override fun onStartTrackingTouch(p0: SeekBar?) {}

            override fun onStopTrackingTouch(p0: SeekBar?) {
                saveLedState("B",p0!!.progress)
            }

        })


        setLedState()
        setButtonState()
    }

    private fun saveLedState(color : String, state : Int){
        val spf = binding.root.context.getSharedPreferences("ledState", MODE_PRIVATE)
        if(spf != null){
            val editor = spf.edit()
            editor.putInt(color,state)
            editor.apply()
        }

    }

    private fun saveButtonState(state : Boolean){
        val spf = binding.root.context.getSharedPreferences("buttonState", MODE_PRIVATE)
        if(spf != null){
            val editor = spf.edit()
            editor.putBoolean("state",state)
            editor.apply()
        }

    }

    private fun setLedState(){
        val spf = binding.root.context.getSharedPreferences("ledState", MODE_PRIVATE)
        if(spf != null){
            binding.RSeekBar.progress = spf.getInt("R",50)
            binding.GSeekBar2.progress = spf.getInt("G",50)
            binding.BSeekBar3.progress = spf.getInt("B",50)
        }

    }

    private fun setButtonState(){
        val spf = binding.root.context.getSharedPreferences("buttonState", MODE_PRIVATE)
        if(spf != null){
            when(spf.getBoolean("state", ledButtonClicked)){
                true -> { // 켜져있을때
                    ledButtonClicked = !ledButtonClicked
                    binding.ledButtonController.text = "OFF"
                    dataModel.setLedOnOFF("ON")
                }
                false ->{ // 꺼져있을때
                    ledButtonClicked = !ledButtonClicked
                    binding.ledButtonController.text = "ON"
                    dataModel.setLedOnOFF("OFF")
                }
            }
        }

    }

    override fun onBackPressed() {
        super.onBackPressed()
        finish()
        overridePendingTransition(R.anim.fade_in,R.anim.fade_out)
    }
}