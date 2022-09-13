## Layout - Breakpoints

- 부트스트랩의 장치 또는 뷰포트 크기에서 반응형 레이아웃이 작동하는 방식을 결정하는 사용자 지정 가능한 너비이다
- **반응형 디자인의 빌딩 블록입니다.** 특정 뷰포트 또는 장치 크기에서 레이아웃을 조정할 수 있는 시기를 제어하는 데 사용합니다.
- 미디어 쿼리를 사용하여 중단점으로 CSS를 설계합니다
- **모바일 우선, 반응형 디자인이 목표입니다**

## Form controls

사용자 정의 스타일, 크기 조정, 포커스 상태 등을 사용하여 input과 같은 텍스트 양식을 업그레이드한다.

### ex)

![image-20220905162741507](C:\Users\조승윤\AppData\Roaming\Typora\typora-user-images\image-20220905162741507.png)

``` 
```

```html
<div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Email address</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
</div>
<div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
</div>
```

### ex) sizing

`.form-control-lg`및 와 같은 클래스를 사용하여 높이를 설정 `.form-control-sm`합니다.

![image-20220905163000142](C:\Users\조승윤\AppData\Roaming\Typora\typora-user-images\image-20220905163000142.png)

```html
<input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" aria-label=".form-control-lg example">
<input class="form-control" type="text" placeholder="Default input" aria-label="default input example">
<input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" aria-label=".form-control-sm example">
```

### ex) Disabled

입력에 부울 속성을 추가하여 `disabled`회색으로 표시하고 포인터 이벤트를 제거하고 초점을 맞추는 것을 방지합니다.

![image-20220905163043363](C:\Users\조승윤\AppData\Roaming\Typora\typora-user-images\image-20220905163043363.png)

```html
<input class="form-control" type="text" placeholder="Disabled input" aria-label="Disabled input example" disabled>
<input class="form-control" type="text" value="Disabled readonly input" aria-label="Disabled input example" disabled readonly>
```

### ex) Readonly

`readonly`입력 값의 수정을 방지하기 위해 입력에 부울 속성을 추가합니다 . `readonly`입력은 계속 초점을 맞추고 선택할 수 있지만 `disabled`입력은 할 수 없습니다.

```html
<input class="form-control" type="text" value="Readonly input here..." aria-label="readonly input example" readonly>
```

### ex) File input

![image-20220905170818393](C:\Users\조승윤\AppData\Roaming\Typora\typora-user-images\image-20220905170818393.png)

```html
<div class="mb-3">
  <label for="formFile" class="form-label">Default file input example</label>
  <input class="form-control" type="file" id="formFile">
</div>
<div class="mb-3">
  <label for="formFileMultiple" class="form-label">Multiple files input example</label>
  <input class="form-control" type="file" id="formFileMultiple" multiple>
</div>
<div class="mb-3">
  <label for="formFileDisabled" class="form-label">Disabled file input example</label>
  <input class="form-control" type="file" id="formFileDisabled" disabled>
</div>
<div class="mb-3">
  <label for="formFileSm" class="form-label">Small file input example</label>
  <input class="form-control form-control-sm" id="formFileSm" type="file">
</div>
<div>
  <label for="formFileLg" class="form-label">Large file input example</label>
  <input class="form-control form-control-lg" id="formFileLg" type="file">
</div>
```

### ex)Datalists (데이터 목록)

자동 완성을 할수 있는 그룹을 만들 수 있다.

![image-20220905170929627](C:\Users\조승윤\AppData\Roaming\Typora\typora-user-images\image-20220905170929627.png)

```html
<label for="exampleDataList" class="form-label">Datalist example</label>
<input class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Type to search...">
<datalist id="datalistOptions">
  <option value="San Francisco">
  <option value="New York">
  <option value="Seattle">
  <option value="Los Angeles">
  <option value="Chicago">
</datalist>
```