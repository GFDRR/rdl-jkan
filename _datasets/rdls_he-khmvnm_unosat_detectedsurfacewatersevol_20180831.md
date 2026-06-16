---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840
dataset_id: rdls_he-khmvnm_unosat_detectedsurfacewatersevol_20180831
description: 'This map illustrates the satellite-detected surface waters extent in
  Long An province and in the southern part of Cambodia, as observed from the Sentinel-1
  SAR images acquired on 16 & 28 August 2018. In the analysed area, an increase of
  surface waters is observed mainly in agricultural and paddy fields areas. In addition,
  using WorldPop data, we can estimate that ~200,000 people are living within or close
  to flooded zones in the province of Long An. It is likely that flood waters have
  been systematically underestimated along highly vegetated areas along main river
  banks and within built-up urban areas because of the special characteristics of
  the satellite data used. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840]'
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
    description: Population living within or close to flooded zones in Long An Province,
      estimated at approximately 200,000 people
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
- asset_type:
    description: Agricultural and paddy field areas affected by surface water inundation
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Satellite analysts compared Sentinel-1 SAR imagery from 16 and 28 August
    2018 to detect changes in surface water extent across Long An Province and southern
    Cambodia. Population exposure was estimated by overlaying the detected flood extent
    with WorldPop gridded population data to quantify people at risk in flooded agricultural
    and built-up areas.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-evolution-in-long-an-province-vietnam-2840
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
  description: Satellite Detected Surface Waters & Evolution in Long An Province,
    Vietnam (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20180830VNM/FL20180830VNM_SHP.zip
  format: null
  id: resource_138d6deb
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
slug: rdls_he-khmvnm_unosat_detectedsurfacewatersevol_20180831
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  - KHM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-08-31'
temporal_resolution: null
title: Satellite Detected Surface Waters & Evolution in Long An Province, Vietnam
version: null
vulnerability: null
---
