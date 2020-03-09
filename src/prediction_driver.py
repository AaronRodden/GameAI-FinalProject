from keras.models import load_model

f = load_model('CNNmodel.h5')

input_ = [213, 193, 127, 120, 117, 116, 116, 115, 116, 118, 119, 135, 147, 151, 156, 157, 165, 169, 170, 173, 177, 182, 186, 193, 199, 203, 201, 207, 216, 209, 168, 123, 119, 117, 116, 115, 115, 116, 117, 122, 144, 150, 155, 158, 157, 164, 165, 168, 171, 175, 180, 185, 192, 197, 202, 189, 219, 211, 204, 143, 121, 117, 116, 116, 115, 116, 116, 118, 133, 149, 153, 157, 152, 156, 158, 160, 162, 166, 169, 173, 179, 184, 189, 172, 221, 212, 205, 191, 127, 119, 116, 116, 115, 115, 116, 118, 121, 144, 152, 156, 153, 140, 148, 149, 151, 153, 155, 158, 161, 164, 167, 162, 221, 210, 201, 193, 161, 121, 118, 116, 115, 115, 115, 117, 119, 131, 151, 155, 152, 134, 127, 128, 128, 129, 129, 131, 133, 138, 142, 147, 194, 188, 182, 177, 173, 139, 120, 117, 115, 115, 115, 116, 118, 121, 145, 153, 150, 133, 128, 131, 133, 134, 135, 137, 139, 141, 144, 148, 196, 189, 183, 178, 175, 169, 126, 117, 115, 114, 115, 116, 118, 120, 130, 151, 149, 131, 129, 131, 134, 134, 136, 138, 139, 142, 145, 148, 193, 186, 181, 177, 174, 170, 153, 121, 116, 114, 114, 115, 117, 119, 122, 143, 146, 129, 129, 130, 132, 134, 136, 139, 140, 141, 143, 146, 189, 183, 178, 175, 170, 164, 159, 136, 118, 115, 114, 115, 115, 118, 121, 129, 145, 126, 126, 128, 131, 134, 137, 137, 138, 139, 140, 143, 185, 180, 176, 171, 164, 159, 153, 148, 125, 115, 114, 114, 115, 116, 120, 121, 137, 124, 126, 129, 130, 134, 138, 144, 149, 154, 161, 171, 183, 180, 171, 162, 153, 145, 139, 135, 127, 117, 115, 115, 114, 116, 118, 122, 125, 128, 133, 138, 145, 152, 163, 176, 184, 191, 201, 217, 192, 187, 178, 163, 150, 139, 131, 127, 123, 119, 115, 114, 114, 115, 117, 121, 124, 134, 148, 157, 165, 169, 181, 190, 199, 206, 217, 231, 184, 199, 199, 195, 191, 190, 187, 185, 181, 176, 129, 114, 115, 115, 116, 118, 123, 134, 174, 184, 191, 187, 198, 199, 204, 211, 220, 231, 144, 188, 202, 201, 197, 195, 192, 187, 182, 178, 166, 119, 114, 114, 115, 117, 121, 126, 155, 180, 188, 188, 190, 197, 201, 207, 215, 225, 144, 146, 191, 200, 199, 196, 193, 188, 184, 180, 176, 151, 115, 114, 114, 115, 117, 124, 132, 175, 184, 187, 180, 187, 187, 191, 197, 204, 140, 145, 152, 184, 184, 180, 177, 173, 169, 165, 159, 156, 128, 113, 113, 114, 117, 121, 126, 152, 180, 183, 177, 170, 173, 177, 183, 191, 137, 142, 155, 177, 178, 176, 173, 170, 166, 163, 159, 156, 152, 119, 113, 114, 115, 118, 123, 129, 172, 178, 171, 168, 173, 178, 182, 189, 135, 140, 163, 176, 176, 174, 173, 170, 166, 162, 158, 156, 153, 139, 113, 112, 114, 116, 119, 126, 144, 173, 164, 164, 169, 176, 180, 187, 138, 138, 173, 177, 176, 174, 172, 168, 164, 161, 159, 153, 147, 140, 124, 112, 113, 114, 117, 121, 126, 160, 157, 157, 163, 171, 179, 185, 162, 146, 176, 176, 175, 173, 170, 165, 162, 160, 153, 146, 139, 134, 127, 114, 111, 112, 115, 117, 122, 132, 140, 144, 150, 157, 167, 177, 134, 159, 167, 171, 169, 166, 162, 157, 153, 150, 143, 133, 126, 122, 119, 117, 112, 110, 112, 114, 117, 123, 129, 139, 145, 149, 158, 165, 143, 131, 143, 132, 123, 123, 124, 124, 136, 160, 157, 154, 152, 150, 148, 146, 134, 111, 110, 112, 114, 119, 125, 147, 154, 154, 152, 155, 124, 126, 120, 129, 119, 113, 115, 118, 115, 127, 132, 131, 129, 128, 126, 125, 124, 116, 109, 111, 113, 115, 121, 132, 151, 151, 143, 144, 109, 111, 118, 120, 125, 122, 113, 114, 113, 123, 129, 129, 128, 126, 124, 124, 124, 123, 113, 111, 111, 114, 116, 122, 144, 148, 141, 145, 112, 112, 114, 117, 127, 132, 128, 113, 112, 125, 126, 127, 128, 128, 127, 125, 123, 121, 117, 112, 111, 112, 114, 119, 128, 144, 136, 140, 110, 110, 112, 112, 114, 138, 144, 138, 115, 123, 123, 125, 125, 124, 124, 124, 123, 119, 114, 112, 112, 113, 113, 115, 119, 134, 131, 135, 119, 122, 126, 129, 132, 140, 173, 161, 167, 161, 158, 158, 155, 153, 151, 145, 135, 127, 122, 119, 116, 113, 112, 114, 117, 121, 129, 137, 152, 163, 165, 169, 173, 176, 182, 186, 178, 206, 161, 159, 158, 158, 184, 182, 175, 171, 166, 162, 157, 121, 114, 114, 115, 119, 138, 147] 

def model_prediction(model, image_input):
    
    label = model.predict(image_input)

    print(label)

    return label

print(f.summary())
print(model_prediction(f, input_))