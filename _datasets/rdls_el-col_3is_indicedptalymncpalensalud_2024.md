---
attributions:
- entity:
    affiliation: null
    email: null
    name: "UNGRD (Unidad Nacional de Gesti\xF3n del Riesgo de Desastres)"
    url: https://data.humdata.org/dataset/indice-dptal-y-mncpal-en-salud-en-el-contexto-del-fenomeno-de-la-nina-en-colombia-2024-ii
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Colombian Health System
    url: https://data.humdata.org/dataset/indice-dptal-y-mncpal-en-salud-en-el-contexto-del-fenomeno-de-la-nina-en-colombia-2024-ii
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Colombian Social Statistics
    url: https://data.humdata.org/dataset/indice-dptal-y-mncpal-en-salud-en-el-contexto-del-fenomeno-de-la-nina-en-colombia-2024-ii
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/indice-dptal-y-mncpal-en-salud-en-el-contexto-del-fenomeno-de-la-nina-en-colombia-2024-ii
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/indice-dptal-y-mncpal-en-salud-en-el-contexto-del-fenomeno-de-la-nina-en-colombia-2024-ii
dataset_id: rdls_el-col_3is_indicedptalymncpalensalud_2024
description: "En este ejercicio se llev\xF3 a cabo un an\xE1lisis de componentes principales\
  \ (PCA, por sus siglas en ingl\xE9s) con el objetivo de realizar una priorizaci\xF3\
  n geogr\xE1fica a nivel departamental y municipal en Colombia. Se utilizaron variables\
  \ relacionadas con la salud, el clima y el contexto socio-demogr\xE1fico para identificar\
  \ y clasificar \xE1reas prioritarias que podr\xEDan verse afectadas por fen\xF3\
  menos clim\xE1ticos como lluvias, deslizamientos, vendavales y avenidas torrenciales.\
  \ Esta priorizaci\xF3n busca facilitar la toma de decisiones en el marco del posible\
  \ Fen\xF3meno de La Ni\xF1a, con un enfoque particular en la capacidad de respuesta\
  \ sanitaria de las regiones priorizadas.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indice-dptal-y-mncpal-en-salud-en-el-contexto-del-fenomeno-de-la-nina-en-colombia-2024-ii]"
details: null
exposure:
- asset_type:
    description: Colombian population at departmental and municipal levels exposed
      to climate hazards and health vulnerabilities
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: "Principal component analysis (PCA) was applied to integrate health\
    \ indicators (malaria, maternal mortality, EDA/IRA, dengue, violence, suicide),\
    \ sociodemographic variables (multidimensional poverty index, conflict-affected\
    \ populations), and climate hazard prioritization data from UNGRD (rainfall, landslides,\
    \ strong winds, torrential flooding) to create a composite vulnerability index\
    \ at departmental and municipal scales. The resulting index prioritizes geographic\
    \ areas in Colombia for humanitarian and health response planning in the context\
    \ of the 2024-II La Ni\xF1a phenomenon."
  sources:
  - id: source_1
    license: null
    name: "UNGRD (Unidad Nacional de Gesti\xF3n del Riesgo de Desastres)"
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Colombian Health System
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Colombian Social Statistics
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indice-dptal-y-mncpal-en-salud-en-el-contexto-del-fenomeno-de-la-nina-en-colombia-2024-ii
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by rainfall-related flooding and associated health
      impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslides and associated health impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by strong winds (vendavales) and associated health
      impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Documentaci\xF3n \xCDndice departamental y municipal de priorizaci\xF3\
    n en salud en el posible marco del Fen\xF3meno de La Ni\xF1a (2024-II).pdf"
  download_url: https://data.humdata.org/dataset/5c1e10e1-ae1b-490f-aa9f-507f621d807d/resource/0a38339d-f5f4-4d87-9f35-f4bf6fb2a65d/download/documentacion-indice-departamental-y-municipal-de-priorizacion-en-salud-en-el-posible-marco-del-.pdf
  format: null
  id: resource_0a38339d
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Documentaci\xF3n \xCDndice departamental y municipal de priorizaci\xF3n\
    \ en salud en el posible marco del Fen\xF3meno de La Ni\xF1a (2024-II).pdf"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia: \xCDndice Dptal y Mncpal en Salud en el Contexto del Fen\xF3\
    meno de La Ni\xF1a (2024-II) (Excel)"
  download_url: https://data.humdata.org/dataset/5c1e10e1-ae1b-490f-aa9f-507f621d807d/resource/2639e3f2-1080-427a-8cf0-f89a5c3c3eb0/download/resultados_departamental_indice.xlsx
  format: null
  id: resource_2639e3f2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Resultados_Departamental_indice.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia: \xCDndice Dptal y Mncpal en Salud en el Contexto del Fen\xF3\
    meno de La Ni\xF1a (2024-II) (Excel)"
  download_url: https://data.humdata.org/dataset/5c1e10e1-ae1b-490f-aa9f-507f621d807d/resource/e75bf96a-3687-43cb-9270-2dc45d5c708b/download/resultados_municipal_indice.xlsx
  format: null
  id: resource_e75bf96a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Resultados_Municipal_indice.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-col_3is_indicedptalymncpalensalud_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-07-31'
  start: '2024-05-31'
temporal_resolution: null
title: "Colombia: \xCDndice Dptal y Mncpal en Salud en el Contexto del Fen\xF3meno\
  \ de La Ni\xF1a (2024-II)"
version: null
vulnerability: null
---
