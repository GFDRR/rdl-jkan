---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-phu-yen-province-2723
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-phu-yen-province-2723
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-phu-yen-province-2723
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-phu-yen-province-2723
dataset_id: rdls_he-vnm_unosat_detectedsurfacewatersexte_20171114
description: 'This map illustrates the satellite-detected surface waters in Phu Yen
  Province, Vietnam, as detected from Sentinel-1 image acquired on 10 November 2017,
  following the landfall of tropical cyclone DAMREY-17 on 05 November 2017. In the
  analysed area, about 19,000 ha of lands are likely flooded. It represents an increase
  of about 100% of the surface waters in this zone. In addition, and according to
  WorldPop data ~39,000 people are living within the potentially flooded areas. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-phu-yen-province-2723]'
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
    description: Approximately 39,000 people living within potentially flooded areas
      based on WorldPop data
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
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR imagery from 10 November 2017 was analyzed by UNOSAT
    to detect surface water extent in Phu Yen Province following tropical cyclone
    DAMREY-17 landfall on 5 November 2017. Multi-temporal satellite image comparison
    identified flooded areas (~19,000 ha, representing 100% increase in surface waters).
    WorldPop gridded population data was overlaid to estimate exposed population (~39,000
    people) in the inundated zone. This is a preliminary post-event damage assessment
    product.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-phu-yen-province-2723
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
  description: Viet Nam - Satellite Detected Surface Waters Extent in Phu Yen Province
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171106VNM/FL20171106VNM_gdb.zip
  format: Geodatabase
  id: resource_3bded516
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171106VNM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Viet Nam - Satellite Detected Surface Waters Extent in Phu Yen Province
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171106VNM/FL20171106VNM_shp.zip
  format: null
  id: resource_03ee50e9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171106VNM_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-vnm_unosat_detectedsurfacewatersexte_20171114
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
  start: '2017-11-14'
temporal_resolution: null
title: Viet Nam - Satellite Detected Surface Waters Extent in Phu Yen Province
version: null
vulnerability: null
---
