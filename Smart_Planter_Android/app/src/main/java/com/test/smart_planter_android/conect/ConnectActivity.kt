package com.test.smart_planter_android.conect

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.test.smart_planter_android.databinding.ActivityConectBinding

class ConnectActivity : AppCompatActivity() {
    lateinit var binding : ActivityConectBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityConectBinding.inflate(layoutInflater)
        setContentView(binding.root)



    }
}