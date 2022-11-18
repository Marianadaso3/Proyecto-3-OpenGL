vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 3)/2000, 1.0)).xyz;
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 3)/2000, 1.0);

}
'''

fragment_shader ='''
#version 450 core
out vec4 fragColor;
in vec2 UVs;
in vec3 norms;
in vec3 pos;
uniform vec3 pointLight;
uniform sampler2D tex;
void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * intensity;
}
'''
red_scale_frag ='''
#version 450 core
out vec4 fragColor;
in vec2 UVs;
in vec3 norms;
in vec3 pos;
uniform vec3 pointLight;
uniform sampler2D tex;
uniform float explodeColor;
void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * intensity;
    float average = (fragColor.x+fragColor.y+fragColor.z)/3;
    fragColor = vec4(average, 0, 0, 1.0); 
}
'''

toon_frag_shadder ='''
#version 450 core
out vec4 fragColor;
in vec2 UVs;
in vec3 norms;
in vec3 pos;
uniform vec3 pointLight;
uniform sampler2D tex;
void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    float toonIntensity = (intensity < 0.3)? 0.1 : (intensity < 0.6) ? 0.5 : (intensity < 0.9) ? 0.8: 1;
    fragColor = texture(tex, UVs) * toonIntensity;
}
'''
