package com.test.smart_planter_android.data_model

import android.content.Context
import android.content.SharedPreferences
import android.net.Uri
import android.util.Log
import androidx.lifecycle.MutableLiveData
import com.google.android.gms.tasks.Tasks
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase
import com.google.firebase.storage.ktx.storage

class DataGet(val context: Context) {
    private val db = Firebase.firestore
    private val storageRef = Firebase.storage.reference
    private var spf : SharedPreferences = context.getSharedPreferences("emName", Context.MODE_PRIVATE)
    private var planterKeyList = ArrayList<String>()
    private var planterStateList = ArrayList<String>()
    private var planterPicList = ArrayList<String>()
    var isok : MutableLiveData<Boolean> = MutableLiveData(false)
    private var count = 0


    fun getDate(){
        val name = spf.getString("eName","default")

        db.collection(name!!+"_t").get().addOnSuccessListener { it ->
            for (date in it){
                planterKeyList.add(date.id)
            }
            count++
            updateChecker()
        }

        db.collection(name!!+"_t").get().addOnSuccessListener { it ->
            for (date in it){
                planterStateList.add(date.data.toString().replace("{","").replace("}","").replace("state=",""))
            }
            count++
            updateChecker()
        }

        storageRef.listAll().addOnSuccessListener { result ->
            // 최상위 10개의 파일을 선택합니다.
            val recentFiles = result.items.take(10)

            val downloadUrlTasks = recentFiles.map { file ->
                file.downloadUrl
            }

            // 선택된 파일들의 다운로드 URL을 가져오거나 필요한 작업을 수행합니다.
            // 모든 다운로드 URL 가져오기 작업이 완료될 때까지 대기합니다.
            Tasks.whenAllSuccess<Uri>(downloadUrlTasks)
                .addOnSuccessListener { downloadUrls ->
                    // 모든 다운로드 URL을 가져온 후에 planterPicList를 업데이트합니다.
                    for (uri in downloadUrls) {
                        val downloadUrl = uri.toString()
                        planterPicList.add(downloadUrl)
                    }
                    count++
                    updateChecker()
                }
        }
    }

    fun getKeyList() : ArrayList<String>{
        if (planterKeyList.size == 0){
            planterKeyList.add("")
        }
        return planterKeyList
    }

    fun getStateList() : ArrayList<String>{
        if (planterStateList.size == 0){
            planterStateList.add("")
        }
        return planterStateList
    }

    fun getPicList() : ArrayList<String>{
        if(planterPicList.size == 0){
            planterPicList.add("")
        }
        planterPicList.reverse()
        return planterPicList
    }

    fun updateChecker(){
        if(count == 3){
            isok.value = true
            count = 0
        }
    }



}