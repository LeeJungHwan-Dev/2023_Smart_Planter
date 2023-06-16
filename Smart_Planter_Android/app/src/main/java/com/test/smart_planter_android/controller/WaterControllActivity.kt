package com.test.smart_planter_android.controller

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.test.smart_planter_android.R
import com.test.smart_planter_android.data_model.DataSend
import com.test.smart_planter_android.databinding.ActivityWaterControllBinding

class WaterControllActivity : AppCompatActivity() {
    private lateinit var binding : ActivityWaterControllBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityWaterControllBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val dateModel = DataSend(binding.root.context)
        binding.timePicker.setIs24HourView(true)


        binding.timeSetButton.setOnClickListener {
            val data = hashMapOf(
                "time" to binding.timePicker.hour.toString() +":"+binding.timePicker.minute.toString()
            )
            dateModel.setTime(data)
            Toast.makeText(this,"시간 설정 완료.",Toast.LENGTH_SHORT).show()
        }


    }

    override fun onBackPressed() {
        super.onBackPressed()
        finish()
        overridePendingTransition(R.anim.fade_in,R.anim.fade_out)
    }
}