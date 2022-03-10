from flask import Flask, render_template, request
import joblib

app=Flask(__name__)
model=joblib.load('model_jlib')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        category=request.form.get('category')
        sub_category=request.form.get('sub_category')
        branded=request.form.get('branded')
        #if category=='select' or sub_category=='select' or branded=='select':
        cols=['Books','Electronics','Fashion','Furniture','Sports','Bed','Chair','Fiction','Home Appliance','Lowers','Non-Fiction','Others','Smartphone','Sports','Table','Upper','Branded']
        sample=[]
        for column in cols:
            if column==category or column==sub_category:
                sample.append(1)
            elif column=='Branded':
                if branded=='yes':
                    sample.append(1)
                else:
                    sample.append(0)
            else:
                sample.append(0)
        ans=model.predict([sample])
        ans=round(ans[0],2)
        txt="The base price for Category: "+category+", Sub Category: "+sub_category+", Branded: "+branded+" is "+str(ans)
        return render_template('home.html',price=txt)

if __name__=='__main__':
    app.run(debug=True)