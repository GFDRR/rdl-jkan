---
attributions:
- entity:
    affiliation: null
    email: null
    name: JIAF (Joint Intersectoral Analysis Framework)
    url: https://data.humdata.org/dataset/pin-intersectorial-colombia-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MIRA/MIRE assessments and WASH baseline surveys
    url: https://data.humdata.org/dataset/pin-intersectorial-colombia-2023
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Secondary sources compilation
    url: https://data.humdata.org/dataset/pin-intersectorial-colombia-2023
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/pin-intersectorial-colombia-2023
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/pin-intersectorial-colombia-2023
dataset_id: rdls_lss-col_immap_pinintersectorial2023
description: "La metodolog\xEDa para el c\xE1lculo de personas en necesidad -PiN-\
  \ intersectorial para el Humanitarian Needs Overview -HNO- 2023 en Colombia, se\
  \ desarroll\xF3 siguiendo la metodolog\xEDa global JIAF (Joint Intersectoral Analysis\
  \ Framework, por sus siglas en ingl\xE9s) en el que se analizan los eventos o shocks\
  \ que afectan las condiciones humanitarias en la poblaci\xF3n a partir de tres pilares:\
  \ i Est\xE1ndares de vida, ii Mecanismos para afrontar el shock y iii Bienestar\
  \ F\xEDsico y Mental. De manera general podr\xE1n encontrar todos los documentos\
  \ utilizados para la construcci\xF3n del PiN y sus desagregaciones.. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/pin-intersectorial-colombia-2023]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The PiN dataset applies the global JIAF methodology to Colombia 2023
    HNO, integrating primary needs assessments (MIRA/MIRE/WASH), secondary indicators
    (conflict incidence, multidimensional poverty), and regional workshop outputs
    to calculate intersectorial people in need across vulnerable groups and municipalities,
    with projections for displacement from armed conflict and natural disasters.
  sources:
  - id: source_1
    license: null
    name: JIAF (Joint Intersectoral Analysis Framework)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: MIRA/MIRE assessments and WASH baseline surveys
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Secondary sources compilation
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pin-intersectorial-colombia-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need (PiN) intersectorial assessment across multiple sectors
      and hazard contexts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Projected population affected by natural disasters including flooding
      and mass displacement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement from armed conflict, confinement, and natural
      disasters
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
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "PiN intersectorial - Colombia 2023 (C\xE1lculo PiN intersectorial,\
    \ Colombia 2023.)"
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/784178c7-6583-448b-b172-79944a9970cb/download/pin-intersectorial-colombia-2023.xlsx
  format: null
  id: resource_784178c7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PIN intersectorial Colombia 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: PiN intersectorial - Colombia 2023 (Consecuencias humanitarias del
    PiN intersectorial, Colombia 2023.)
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/5a97db62-27ed-4d00-abdc-b1f7f4d252ce/download/consecuencias-humanitaria-pin-intersectorial-colombia-2023.xlsx
  format: null
  id: resource_5a97db62
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Consecuencias humanitaria - PiN intersectorial Colombia 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "PiN intersectorial - Colombia 2023 (Desagregaci\xF3n de los grupos\
    \ vulnerables del PiN intersectorial, Colombia 2023.)"
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/5b4ab205-a3e6-41ec-b013-0c2173dfacc2/download/desagregacion-grupos-vulnerables-pin-intersectorial-2023-colombia.xlsx
  format: null
  id: resource_5b4ab205
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Desagregaci\xF3n grupos vulnerables - PiN intersectorial 2023 Colombia.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "PiN intersectorial - Colombia 2023 (Resultados del PiN intersectorial\
    \ y PiN por cl\xFAster, Colombia 2023.)"
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/69b8734a-5cf3-465e-b564-432e69150937/download/resultados-pin-intersectorial-y-sectorial-por-municipio-pin-2023-colombia.xlsx
  format: null
  id: resource_69b8734a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Resultados PIN intersectorial y PiN por cl\xFAster por Municipio - PiN 2023\
    \ Colombia.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Resumen de indicadores seleccionados por los cl\xFAster para la construcci\xF3\
    n de cada PiN, Colombia 2023."
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/b8dc5d76-b5dd-406e-bf2c-ba9e6d8af1f4/download/resumen-indicadores-seleccionados-por-cluster-pin-2023.xlsx
  format: null
  id: resource_b8dc5d76
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Resumen indicadores seleccionados por cl\xFAster PiN 2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Resultados de los talleres regionales HNO 2022 . Nota: Estos datos\
    \ son importantes para el c\xE1lculo del PiN ya que se considera como el 'Juicio\
    \ de expertos'."
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/17924f1a-50f0-4ef2-9fb3-a34eaa62b1a9/download/resultados-totales-regionales-hno-2022.xlsx
  format: null
  id: resource_17924f1a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Resultados talleres regionales HNO 2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "PiN intersectorial - Colombia 2023 (C\xE1lculo de comunidades de acogida\
    \ 2022 - 2023, Colombia.)"
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/114272ae-571e-40e3-b40a-04bb5760ab98/download/comunidades-anfitrionas-nueva-metodologia-2022-2023.xlsx
  format: null
  id: resource_114272ae
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Comunidades de acogida 2022 - 2023 Colombia.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "PiN intersectorial - Colombia 2023 (C\xE1lculo del \xEDndice de 'Incidencia\
    \ del Conflicto Armado 2022 - 2023 Colombia'.)"
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/0cafa3ff-6747-439a-b54c-0a221d850deb/download/indicador-incidencia-del-conflicto-armado-2022-2023-colombia.xlsx
  format: null
  id: resource_0cafa3ff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Indicador Incidencia del Conflicto Armado 2022 - 2023 Colombia.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "PiN intersectorial - Colombia 2023 (C\xE1lculo del \xEDndice de 'Pobreza\
    \ Multidimensional 2022 - 2023 Colombia'.)"
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/657347f7-c7b3-451e-aaa1-f490c4446781/download/indicador-de-pobreza-multidimensional-2022-2023-colombia.xlsx
  format: null
  id: resource_657347f7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Indicador de Pobreza Multidimensional 2022 - 2023 Colombia.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Severidades de las evaluaciones de necesidades MIRA-MIRE-L\xEDnea\
    \ de base WASH 2021-2022, Colombia."
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/652752d1-ef00-4953-951a-99f7f44c19b1/download/severidades-evaluaciones-de-necesidades-mira-mire-linea-de-base-wash-2021-2022-colombia.xlsx
  format: null
  id: resource_652752d1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Severidad evaluaciones de necesidades MIRA-MIRE-L\xEDnea de base WASH 2021-2022\
    \ Colombia.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene informaci\xF3n de fuentes secundarias utilizadas\
    \ para el c\xE1lculo del PiN Intersectorial, con corte del 1 enero 2021 a 30 de\
    \ junio 2022. La informaci\xF3n contiene: delitos sexuales, afectaciones por artefactos\
    \ explosivos, afectaciones por desastres de origen natural, desplazamiento individual,\
    \ desplazamiento masivo, vinculaci\xF3n de ni\xF1os, ni\xF1as y adolescentes a\
    \ actividades relacionadas con grupos armados, confinamiento y ataques contra\
    \ la poblaci\xF3n civil."
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/a9cad02c-d52f-4598-809f-402f026cfc85/download/informacion-fuentes-secundarias-calculo-del-pin-intersecrorial-2023.xlsx
  format: null
  id: resource_a9cad02c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Informaci\xF3n fuentes secundarias - C\xE1lculo del PiN Intersecrorial 2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Nota metodol\xF3gica del procedimiento del c\xE1lculo del PiN intersectorial,\
    \ Colombia 2023."
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/c8abc69e-c0f8-4e12-9f25-6144c858d2a7/download/nota-metodologica-pin-intersectorial-2023.pdf
  format: null
  id: resource_c8abc69e
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Nota Metodol\xF3gica - PiN intersectorial 2023.pdf"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Nota metodol\xF3gica del procedimiento del c\xE1lculo de las desagregaciones\
    \ de grupos vulnerables del PiN intersectorial, Colombia 2023."
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/f690a0bf-a887-40cc-992e-ca133c7a344c/download/nota-metodologica-desagregacion-grupos-vulnerables-pin-intersectorial-2023.pdf
  format: null
  id: resource_f690a0bf
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Nota Metodol\xF3gica - Desagregaci\xF3n grupos vulnerables PiN intersectorial\
    \ 2023.pdf"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Nota metodol\xF3gica del procedimiento de proyecciones sobre afectaciones\
    \ por desplazamiento masivo, confinamiento y desastres de origen natural para\
    \ el a\xF1o 2023."
  download_url: https://data.humdata.org/dataset/715d68eb-6d10-4ba9-8065-6209d38aa3ea/resource/ed0df3e0-e67a-479e-9779-1d98a6d346c9/download/nota-metodologica-proyeciones-afectacion-por-desplazamiento-masivo_confinamiento_desastres-de-or.pdf
  format: null
  id: resource_ed0df3e0
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Nota Metodol\xF3gica - Proyeciones afectaci\xF3n por desplazamiento masivo_confinamiento_desastres\
    \ de origen natural.pdf"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_immap_pinintersectorial2023
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: PiN intersectorial - Colombia 2023
version: null
vulnerability: null
---
