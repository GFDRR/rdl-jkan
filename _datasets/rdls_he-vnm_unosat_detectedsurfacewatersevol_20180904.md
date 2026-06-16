---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-southern-provinces-of-kien-giang-dong-thap-an-giang-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-southern-provinces-of-kien-giang-dong-thap-an-giang-
dataset_id: rdls_he-vnm_unosat_detectedsurfacewatersevol_20180904
description: 'This map illustrates the satellite-detected surface waters extent in
  the southern provinces of kien Giang, An Giang, Dong Thap & Can tho as observed
  from the Sentinel-1 SAR images acquired on 16 & 28 August 2018. In the analysed
  area, an increase of surface waters is observed mainly in agricultural and paddy
  fields areas. It is likely that flood waters have been systematically underestimated
  along highly vegetated areas along main river banks and within built-up urban areas
  because of the special characteristics of the satellite data used. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-southern-provinces-of-kien-giang-dong-thap-an-giang-]'
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
    description: Agricultural and paddy field areas in the study region
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Built-up urban areas in the southern provinces
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR satellite images acquired on 16 and 28 August 2018 were
    analyzed by UNOSAT analysts through visual comparison to detect changes in surface
    water extent. The resulting flood inundation map delineates areas of increased
    surface water in agricultural, paddy field, and urban areas across Kien Giang,
    An Giang, Dong Thap, and Can Tho provinces.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-southern-provinces-of-kien-giang-dong-thap-an-giang-
  rel: source
loss: null
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
  description: Satellite Detected Surface Waters Evolution in Southern Provinces of
    Kien Giang, Dong Thap & An Giang, Vietnam (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20180830VNM/FL20180830VNM_SHP.zip
  format: null
  id: resource_1c845d11
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180830VNM_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-vnm_unosat_detectedsurfacewatersevol_20180904
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-09-04'
temporal_resolution: null
title: Satellite Detected Surface Waters Evolution in Southern Provinces of Kien Giang,
  Dong Thap & An Giang, Vietnam
version: null
vulnerability: null
---
