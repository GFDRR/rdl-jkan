---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/impact-des-glissements-de-terrain-le-7-mai-2023-en-territoire-de-kalehe-province-du-sud-ki
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-glissements-de-terrain-le-7-mai-2023-en-territoire-de-kalehe-province-du-sud-ki
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-glissements-de-terrain-le-7-mai-2023-en-territoire-de-kalehe-province-du-sud-ki
dataset_id: rdls_hl-cod_unosat_impactdesglissementsdeter_20230508
description: "UNOSAT code FL20230508COD, GDACS Id: 1101981 Cette carte illustre l'\xE9\
  tendue des glissements de terrain le 07 mai 2023 en Territoire de Kalehe, Province\
  \ du Sud-Kivu, R\xE9publique D\xE9mocratique du Congo. Dans la zone analys\xE9e\
  \ de 9,000 ha, environ 90 ha d'escarpements de glissements de terrain sont visibles.\
  \ Ceci est une analyse pr\xE9liminaire et n'a pas \xE9t\xE9 valid\xE9e sur le terrain.\
  \ Merci d'envoyer vos commentaires au Centre Satellitaire des Nations Unies (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/impact-des-glissements-de-terrain-le-7-mai-2023-en-territoire-de-kalehe-province-du-sud-ki]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: landslide_general
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from before
    and after the 7 May 2023 landslide event in Kalehe Territory, identifying notable
    changes in terrain to delineate landslide scarp boundaries. The analysis mapped
    approximately 90 hectares of visible landslide escarpments within a 9,000 hectare
    study area, producing vector geometries with area measurements. This is a preliminary
    post-event impact assessment not yet validated on the ground.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/impact-des-glissements-de-terrain-le-7-mai-2023-en-territoire-de-kalehe-province-du-sud-ki
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct landslide scarp extent and area affected in the study zone
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
  description: "Impact des glissements de terrain le 7 mai 2023 en Territoire de Kalehe,\
    \ Province du Sud-Kivu, R\xE9publique D\xE9mocratique du Congo (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3577/FL20230508COD_gdb.zip
  format: Geodatabase
  id: resource_192dee73
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230508COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Impact des glissements de terrain le 7 mai 2023 en Territoire de Kalehe,\
    \ Province du Sud-Kivu, R\xE9publique D\xE9mocratique du Congo (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3577/FL20230508COD_SHP.zip
  format: null
  id: resource_f5951141
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230508COD_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cod_unosat_impactdesglissementsdeter_20230508
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-08'
temporal_resolution: null
title: "Impact des glissements de terrain le 7 mai 2023 en Territoire de Kalehe, Province\
  \ du Sud-Kivu, R\xE9publique D\xE9mocratique du Congo"
version: null
vulnerability: null
---
