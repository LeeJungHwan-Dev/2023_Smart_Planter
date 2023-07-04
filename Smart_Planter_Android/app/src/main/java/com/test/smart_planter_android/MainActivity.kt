package com.test.smart_planter_android

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import com.test.smart_planter_android.conect.ConnectActivity
import com.test.smart_planter_android.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    lateinit var binding : ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        var runnable = Runnable {
            var intent = Intent(this,ConnectActivity::class.java)
            startActivity(intent)
            overridePendingTransition(R.anim.fade_in,R.anim.fade_out)
            finish()
        }

        Handler(Looper.getMainLooper()).postDelayed(runnable,1000)



    }

}