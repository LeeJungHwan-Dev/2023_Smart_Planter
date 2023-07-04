package com.test.smart_planter_android.conect

import android.content.Intent
import android.content.SharedPreferences
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.test.smart_planter_android.R
import com.test.smart_planter_android.controller.PlanterControllerActivity
import com.test.smart_planter_android.databinding.ActivityConectBinding

class ConnectActivity : AppCompatActivity() {
    lateinit var binding : ActivityConectBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityConectBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.CheckButton.setOnClickListener {
            saveEmName(binding.connectInputBox.text.toString())
            var intent = Intent(this,PlanterControllerActivity::class.java)
            startActivity(intent)
            finish()
            overridePendingTransition(R.anim.fade_in,R.anim.fade_out)
        }

    }

    fun saveEmName(name : String){
        var spf = getSharedPreferences("emName", MODE_PRIVATE)
        if(spf.getString("eName","default") == "default") {
            val editor = spf.edit()
            editor.putString("eName", name)
            editor.apply()
        }
    }


}