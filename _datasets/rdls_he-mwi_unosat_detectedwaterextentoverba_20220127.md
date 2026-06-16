---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-balaka-neno-and-zomba-districts-southern-region-malawi-as-of-26-january-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-balaka-neno-and-zomba-districts-southern-region-malawi-as-of-26-january-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-balaka-neno-and-zomba-districts-southern-region-malawi-as-of-26-january-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-balaka-neno-and-zomba-districts-southern-region-malawi-as-of-26-january-
dataset_id: rdls_he-mwi_unosat_detectedwaterextentoverba_20220127
description: 'UNOSAT code: TC20220126MWI This map illustrates satellite-detected surface
  waters in Balaka, Blantyre, Neno, and Zomba districts, Southern region, Malawi as
  observed from a Sentinel-1 image acquired on 26 January 2021 at 05:16 local time
  and using an automated analysis with Artificial Intelligence based methods. Within
  the analyzed area of about 1,000 km2, about 28 km2 of lands appear to be flooded.
  Based on Worldpop population data and the detected surface waters in the analyzed
  area, about 5,400 people are potentially exposed or living close to flooded areas.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT) . Important note:
  Flood analysis from radar images may underestimate the presence of standing waters
  in built-up areas and densely vegetated areas due to backscattering properties of
  the radar signal.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-balaka-neno-and-zomba-districts-southern-region-malawi-as-of-26-january-]'
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
    description: Population potentially exposed or living close to detected flooded
      areas based on WorldPop data
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
  description: "Sentinel-1 SAR satellite imagery acquired on 26 January 2022 was processed\
    \ using automated AI-based analysis methods to detect surface water extent. The\
    \ resulting water polygons (28 km\xC2\xB2 total) were intersected with WorldPop\
    \ gridded population data to estimate approximately 5,400 people potentially exposed\
    \ to flooded areas across the three districts."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
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
- href: https://data.humdata.org/dataset/water-extent-over-balaka-neno-and-zomba-districts-southern-region-malawi-as-of-26-january-
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
  description: Satellite detected water extent over Balaka, Neno and Zomba districts,
    Southern region, Malawi as of 26 January 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_gdb.zip
  format: Geodatabase
  id: resource_a019414c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220126MWI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Balaka, Neno and Zomba districts,
    Southern region, Malawi as of 26 January 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MW/TC20220126MWI/TC20220126MWI_SHP.zip
  format: null
  id: resource_12997a9b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220126MWI_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mwi_unosat_detectedwaterextentoverba_20220127
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-01-27'
temporal_resolution: null
title: Satellite detected water extent over Balaka, Neno and Zomba districts, Southern
  region, Malawi as of 26 January 2022
version: null
vulnerability: null
---
