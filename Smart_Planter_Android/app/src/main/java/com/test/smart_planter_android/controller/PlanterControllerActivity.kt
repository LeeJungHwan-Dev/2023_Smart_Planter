package com.test.smart_planter_android.controller

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.MotionEvent
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.Observer
import androidx.recyclerview.widget.LinearLayoutManager
import com.test.smart_planter_android.R
import com.test.smart_planter_android.data_model.DataGet
import com.test.smart_planter_android.databinding.ActivityPlanterControllerBinding

class PlanterControllerActivity : AppCompatActivity() {
    private lateinit var binding : ActivityPlanterControllerBinding
    private lateinit var adapter: PlanterAdapter
    private var keyList = ArrayList<String>()
    private var stateList = ArrayList<String>()
    private var picList = ArrayList<String>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPlanterControllerBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val getServerDate = DataGet(binding.root.context)

        binding.ledButton.setOnTouchListener { view, motionEvent ->
            when(motionEvent.action){
                MotionEvent.ACTION_DOWN -> {
                    binding.ledButton.alpha = 0.5f
                    true
                }

                MotionEvent.ACTION_UP ->{
                    binding.ledButton.alpha = 1.0f

                    val intent = Intent(this,LedControllActivity::class.java)
                    startActivity(intent)
                    overridePendingTransition(R.anim.fade_in,R.anim.fade_out)

                    true
                }
                else -> false
            }
        }

        binding.waterButton.setOnTouchListener { view, motionEvent ->
            when(motionEvent.action){
                MotionEvent.ACTION_DOWN -> {
                    binding.waterButton.alpha = 0.5f
                    true
                }

                MotionEvent.ACTION_UP ->{
                    binding.waterButton.alpha = 1.0f

                    val intent = Intent(this,WaterControllActivity::class.java)
                    startActivity(intent)
                    overridePendingTransition(R.anim.fade_in,R.anim.fade_out)

                    true
                }
                else -> false
            }
        }


        val list = Observer<Boolean>{
            if(it == true){
                keyList = getServerDate.getKeyList()
                stateList = getServerDate.getStateList()
                picList = getServerDate.getPicList()

                adapter = PlanterAdapter(binding.root.context, picList, keyList, stateList)
                binding.photoList.adapter = adapter
                binding.photoList.layoutManager = LinearLayoutManager(this@PlanterControllerActivity, LinearLayoutManager.HORIZONTAL, false)
                adapter.notifyDataSetChanged()
            }
        }

        getServerDate.isok.observe(this,list)

        getServerDate.getDate()




    }

    override fun onBackPressed() {
        super.onBackPressed()
        overridePendingTransition(R.anim.fade_in,R.anim.fade_out)
    }
}