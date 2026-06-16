---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Comisi\xF3n Interinstitucional para la Protecci\xF3n de las Personas Desplazadas\
      \ por la Violencia (CIPPDV)"
    url: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Instituto Nacional de Estad\xEDstica (INE) Honduras"
    url: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ACNUR (UNHCR)
    url: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Joint IDP Profiling Service (JIPS)
    url: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Joint IDP Profiling Service (JIPS) (inactive)
  url: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras
creator:
  affiliation: null
  email: null
  name: Joint IDP Profiling Service (JIPS) (inactive)
  url: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras
dataset_id: rdls_lss-hnd_jips_informedecaracterizaciond_2014
description: "Caracterizaci\xF3n de poblaci\xF3n desplazada debido a la criminalidad\
  \ en centros urbanos de Honduras (20 municipios). Informaci\xF3n de 1,300 hogares\
  \ desplazados internos y 838 hogares de comparaci\xF3n (no desplazados). Ejercicio\
  \ liderado por la Comisi\xF3n Interinstitucional para la Protecci\xF3n de las Personas\
  \ Desplazadas por la Violencia (Honduras), con el apoyo del INE (Honduras), ACNUR\
  \ y JIPS. La informaci\xF3n puede ser analizada f\xE1cilmente en el DART: http://www.dart.jips.org/..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras]"
details: "_Limitantes_: Al ser un problema emergente e invisible, la disponibilidad\
  \ de informaci\xF3n secundaria sobre el tema fue limitada, para realizar un mayor\
  \ an\xE1lisis en el momento de determinar las zonas para el dise\xF1o muestral.\
  \ Ausencia de la poblaci\xF3n en sus hogares: Por lo general, durante el d\xEDa,\
  \ la poblaci\xF3n est\xE1 en sus lugares de trabajo. Por otro lado, para garantizar\
  \ la seguridad de los equipos de terreno, el trabajo se terminaba a m\xE1s tardar\
  \ a las 5:00 p.m. Esto implic\xF3 que los hogares sin informaci\xF3n fueran casi\
  \ el 50% de los hogares enumerados. Obst\xE1culos para el acceso a zonas de alto\
  \ riesgo, debido a conflictos sociales no resueltos (maras, pandillas, crimen organizado,\
  \ luchas por control territorial, narcotr\xE1fico, etc.). Las poblaciones tienden,\
  \ adem\xE1s, a negarse a dar informaci\xF3n que pueda comprometer su seguridad personal\
  \ y la de su familia. Dados los recursos limitados para el ejercicio, fue imposible\
  \ ir a todos los departamentos del pa\xEDs. Por tal raz\xF3n los estimados realizados\
  \ tienen alcance s\xF3lo para los 11 departamentos visitados; e) Por el car\xE1\
  cter de las zonas enumeradas se puede estar perdiendo el perfil rural del desplazamiento."
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: In 2014, a collaborative exercise led by CIPPDV with technical support
    from JIPS and ACNUR collected household-level data on 1,300 internally displaced
    households and 838 comparison non-displaced households across 20 municipalities
    in Honduras. The data characterizes displacement patterns, demographics, and vulnerabilities
    resulting from violence-related insecurity in urban centers, with results accessible
    through the DART platform.
  sources:
  - id: source_1
    license: null
    name: "Comisi\xF3n Interinstitucional para la Protecci\xF3n de las Personas Desplazadas\
      \ por la Violencia (CIPPDV)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Instituto Nacional de Estad\xEDstica (INE) Honduras"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: ACNUR (UNHCR)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Joint IDP Profiling Service (JIPS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/informe-de-caracterizacion-del-desplazamiento-interno-en-honduras
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons due to violence-related insecurity in
      urban centers
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
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
  description: This dataset includes a description of the methodology, a metadata
    list to guide users to understanding the variables in the dataset, and the dataset
    itself which includes household and individual-level data.
  download_url: https://data.humdata.org/dataset/3fcbc981-5858-46c4-9bef-9f87c68c0bc2/resource/9d55205a-1a4b-4172-bb66-e9c265d7bb8a/download/honduras_final_dataset_for_dart.xlsx
  format: null
  id: resource_9d55205a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Honduras_Final_dataset_for_DART.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_jips_informedecaracterizaciond_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2014-12-31'
  start: '2014-08-01'
temporal_resolution: null
title: "Honduras - Informe de Caracterizaci\xF3n del Desplazamiento Interno"
version: null
vulnerability: null
---
