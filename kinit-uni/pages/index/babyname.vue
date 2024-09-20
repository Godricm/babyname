<template>
	<view>
		<form>
			<view class="cu-form-group margin-top">
				<view class="title">姓氏</view>
				<input placeholder="请输入姓氏,如:赵" name="input" v-model="lastName"></input>
			</view>
			<view class="cu-form-group">
				<view class="title">出生状态</view>
				<switch disabled="true" @change="SwitchA" :class="switchA?'checked':''" :checked="switchA?true:false">
				</switch>
			</view>
			<radio-group class="block" @change="RadioChange">
				<view class="cu-form-group">
					<view class="title">性别</view>
					<view>
						<radio class='blue radio' :class="radio=='未知'?'checked':''" :checked="radio=='C'?true:false"
							value="未知">
							未知</radio>
						<radio class='red margin-left-sm' :class="radio=='男'?'checked':''"
							:checked="radio=='D'?true:false" value="男">男
						</radio>
						<radio class='red margin-left-sm' :class="radio=='女'?'checked':''"
							:checked="radio=='E'?true:false" value="女">女
						</radio>
					</view>
				</view>
			</radio-group>
			<view class="cu-form-group">
				<view class="title">国风选择</view>
				<picker @change="PickerChange" :value="index" :range="picker">
					<view class="picker">
						{{index>-1?picker[index]:'禁止换行，超出容器部分会以 ... 方式截断'}}
					</view>
				</picker>
			</view>
		<button class="cu-btn bg-red margin-tb-sm lg" @click="babyname">国风取名</button>
		</form>
	</view>
</template>

<script>
	import {
		wxLoginMixins
	} from '@/common/mixins/auth.js'
	import {
		createName
	} from '@/common/request/api/babyname/babyname.js'
	export default {
		data() {
			return {
				lastName: "",
				switchA: false,
				radio: '未知',
				index: 0,
				picker: ["默认", "诗经", "楚辞", "论语", "周易", "唐诗", "宋诗", "宋词"],
			}
		},
		mixins: [wxLoginMixins],
		methods: {
			RadioChange(e) {
				this.radio = e.detail.value
			},
			PickerChange(e) {
				this.index = e.detail.value
			},
			babyname() {
				createName(this.lastName, this.radio, this.index).then(res => {
						this.status = res.data
					})
					.finally(() => {
						this.btnLoading = false
					});
			}
		}
	}
</script>

<style>
	.cu-form-group .title {
		min-width: calc(4em + 15px);
	}
</style>