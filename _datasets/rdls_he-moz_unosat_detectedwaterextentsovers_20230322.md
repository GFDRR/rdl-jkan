---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-21-march-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-21-march-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-21-march-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-21-march-2023
dataset_id: rdls_he-moz_unosat_detectedwaterextentsovers_20230322
description: "UNOSAT code TC20230221MOZ, GDACS Id: 1000961 This map illustrates satellite-detected\
  \ water using Sentinel-2 acquired on 21 March 2023, 09:55 local time over the intersection\
  \ between Shire river and Zambezi rivers in Sofala, Tete and Zambezia Provinces\
  \ of Mozambique. Within the cloud free analyzed areas of about 20,000 km\xB2, a\
  \ total of about 2,400 km\xB2 of lands appear to be affected with flood waters.\
  \ Based on Worldpop population data and flood water extent, ~180,000 people are\
  \ potentially exposed or living close to flooded areas mainly located in Mutarara\
  \ district, Tete province with ~62,000 people, Caia district, Sofala province with\
  \ ~38,200 people and Mopeia district, Zambezia province with ~34,000 people This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-21-march-2023]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population potentially exposed to flood waters based on WorldPop
      data, approximately 180,000 people in Mutarara district and surrounding areas
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
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Sentinel-2 multispectral imagery acquired\
    \ on 21 March 2023 to detect water extent through spectral analysis and manual\
    \ interpretation, delineating flooded areas across 20,000 km\xB2 of cloud-free\
    \ terrain. Population exposure was estimated by intersecting the flood water extent\
    \ polygons with WorldPop gridded population data to quantify potentially affected\
    \ populations in Sofala, Tete, and Zambezia provinces."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-over-sofala-tete-and-zambezia-provinces-mozambique-as-of-21-march-2023
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extents over Sofala, Tete, and Zambezia Provinces,
    Mozambique as of 21 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3541/TC20230221MOZ_gdb.zip
  format: Geodatabase
  id: resource_3d943fcd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Sofala, Tete, and Zambezia Provinces,
    Mozambique as of 21 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3541/TC20230221MOZ_shp.zip
  format: null
  id: resource_23fb6732
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Sofala, Tete, and Zambezia Provinces,
    Mozambique as of 21 March 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3541/UNOSAT_Population_Exposure_TC20230221MOZ_21Mar23_Mozambique.xlsx
  format: null
  id: resource_cfbde925
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20230221MOZ_21Mar23_Mozambique.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextentsovers_20230322
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-22'
temporal_resolution: null
title: Satellite detected water extents over Sofala, Tete, and Zambezia Provinces,
  Mozambique as of 21 March 2023
version: null
vulnerability: null
---
