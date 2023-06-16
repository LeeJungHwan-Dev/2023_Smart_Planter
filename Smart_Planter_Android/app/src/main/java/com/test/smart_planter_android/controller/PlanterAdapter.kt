package com.test.smart_planter_android.controller

import android.content.Context
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.test.smart_planter_android.databinding.PlanterPhotoBinding

class PlanterAdapter(private val context: Context, private val planterPicList: ArrayList<String> ,  private val dateList : ArrayList<String>,private val stateList : ArrayList<String>) :
    RecyclerView.Adapter<PlanterAdapter.PlanterViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PlanterViewHolder {
        val inflater = LayoutInflater.from(context)
        val binding = PlanterPhotoBinding.inflate(inflater, parent, false)
        return PlanterViewHolder(binding)
    }

    override fun onBindViewHolder(holder: PlanterViewHolder, position: Int) {
        holder.bind(position)
    }

    override fun getItemCount(): Int {
        return planterPicList.size
    }

    inner class PlanterViewHolder(private val binding: PlanterPhotoBinding) :
        RecyclerView.ViewHolder(binding.root) {

        fun bind(pos:Int) {
            Glide.with(binding.root).load(planterPicList[pos])
                .thumbnail(0.25f)
                .into(binding.flowerPic)
            binding.picDate.text = "날짜 : ${dateList[pos]}"
            binding.flowerState.text = "${stateList[pos]}"
        }
    }
}