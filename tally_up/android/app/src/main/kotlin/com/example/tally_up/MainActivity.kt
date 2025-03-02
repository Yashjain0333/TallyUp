package com.example.tally_up

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Build
import android.provider.Telephony
import android.net.Uri
import java.util.Calendar
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.EventChannel
import io.flutter.plugin.common.MethodChannel

class MainActivity: FlutterActivity() {
    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        
        val methodChannel = MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example.tally_up/sms")
        
        methodChannel.setMethodCallHandler { call, result ->
            when (call.method) {
                "readMonthSMS" -> {
                    try {
                        val messages = readMonthSMS()
                        result.success(messages)
                    } catch (e: Exception) {
                        result.error("SMS_READ_ERROR", e.message, null)
                    }
                }
                else -> result.notImplemented()
            }
        }
    }

    private fun readMonthSMS(): List<Map<String, String>> {
        val messages = mutableListOf<Map<String, String>>()
        val calendar = Calendar.getInstance()
        calendar.set(Calendar.DAY_OF_MONTH, 1)
        calendar.set(Calendar.HOUR_OF_DAY, 0)
        calendar.set(Calendar.MINUTE, 0)
        calendar.set(Calendar.SECOND, 0)
        val monthStart = calendar.timeInMillis

        val cursor = contentResolver.query(
            Uri.parse("content://sms/inbox"),
            arrayOf("body", "address", "date"),
            "date >= ?",
            arrayOf(monthStart.toString()),
            "date DESC"
        )

        cursor?.use {
            val bodyIndex = it.getColumnIndex("body")
            val addressIndex = it.getColumnIndex("address")
            val dateIndex = it.getColumnIndex("date")

            while (it.moveToNext()) {
                val messageMap = mapOf(
                    "message" to (it.getString(bodyIndex) ?: ""),
                    "sender" to (it.getString(addressIndex) ?: "Unknown"),
                    "date" to (it.getString(dateIndex) ?: "0")
                )
                messages.add(messageMap)
            }
        }

        return messages
    }
}