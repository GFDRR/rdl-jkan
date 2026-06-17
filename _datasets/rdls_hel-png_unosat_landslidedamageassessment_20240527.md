---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/landslide-damage-assessment-in-the-lagaip-pogera-district-enga-province-as-of-27-may-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/landslide-damage-assessment-in-the-lagaip-pogera-district-enga-province-as-of-27-may-2024
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GeoEye-1
    url: https://data.humdata.org/dataset/landslide-damage-assessment-in-the-lagaip-pogera-district-enga-province-as-of-27-may-2024
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-damage-assessment-in-the-lagaip-pogera-district-enga-province-as-of-27-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-damage-assessment-in-the-lagaip-pogera-district-enga-province-as-of-27-may-2024
dataset_id: rdls_hel-png_unosat_landslidedamageassessment_20240527
description: 'UNOSAT code: LS20240525PNG, GDACS ID: 1102646 This map illustrates the
  extent of satellite-detected landslide scars and related damage in the Lagaip/Pogera
  District of Enga Province in Papua New Guinea, using GeoEye-1 satellite imagery
  acquired on May 27, 2024, at 10:42 LT, 2 km west of Mulitaka. A massive landslide
  and rockfalls have affected the area. Within a 2 km radius, 634 pre-event structures
  have been identified (OpenStreetMap), of which at least 18 structures have been
  identified as damaged and/or destroyed. Using WorldPop spatial demographic datasets,
  it is estimated that at least 2,000 people live within a 2 km radius of the main
  damaged road. The main landslide scar covers approximately 9 hectares and has also
  blocked the Laiagam-Porgera road. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to the United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-damage-assessment-in-the-lagaip-pogera-district-enga-province-as-of-27-may-2024]'
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
    description: Pre-event building stock identified from OpenStreetMap within 2 km
      radius of the landslide event (634 structures)
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Residential population estimated using WorldPop spatial demographic
      datasets
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: LSI:-
      process: landslide_rockslide
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts conducted post-event damage assessment by comparing
    satellite imagery (GeoEye-1, 27 May 2024) to identify landslide scars and structural
    damage. Pre-event building inventory from OpenStreetMap and population estimates
    from WorldPop were overlaid to quantify exposure. Direct damage counts were derived
    from visual interpretation of satellite-detected changes in building structures.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: GeoEye-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-damage-assessment-in-the-lagaip-pogera-district-enga-province-as-of-27-may-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide and rockfall event with 18
      structures identified as damaged and/or destroyed
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: Papua New Guinea - Landslide damage assessment in the Lagaip/Pogera
    District, Enga Province as of 27 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3857/LS20240525PNG_gdb.zip
  format: Geodatabase
  id: resource_6c5a163a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240525PNG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Papua New Guinea - Landslide damage assessment in the Lagaip/Pogera
    District, Enga Province as of 27 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3857/LS20240525PNG_SHP.zip
  format: null
  id: resource_f0e244f8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240525PNG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-png_unosat_landslidedamageassessment_20240527
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-27'
temporal_resolution: null
title: Papua New Guinea - Landslide damage assessment in the Lagaip/Pogera District,
  Enga Province as of 27 May 2024
version: null
vulnerability: null
---
