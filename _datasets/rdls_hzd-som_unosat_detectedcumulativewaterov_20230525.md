---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023
dataset_id: rdls_hzd-som_unosat_detectedcumulativewaterov_20230525
description: 'UNOSAT code FL20230327SOM, GDACS Id: 1101908 This map illustrates the
  cumulative satellite-detected water affected sectors of Beledweyne City in Hiiran
  Region, Somalia as detected from the analysis of a satellite Jilin-1 images acquired
  on 12 May 2023 and Pleiades acquired on 25 May 2023. Beletweyne is heavily affected
  by floods and about 67% of the town and its vicinity is largely inundated; the sectors
  called Kutimbo Neighborhood and Lamagalay Regional Military Base appear to be the
  most affected by floodwaters. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT). [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (Jilin-1
    on 12 May 2023 and Pleiades on 25 May 2023) to detect and delineate cumulative
    water extent across Beledweyne City during the May 2023 flood event. Water-affected
    polygons were classified with confidence levels and validated against field observations
    where available.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cumulative-water-over-beledweyne-city-hiraan-region-of-somalia-between-12-and-25-may-2023
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
  description: Satellite detected cumulative water over Beledweyne City, Hiraan Region
    of Somalia between 12 and 25 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3599/FL20230327SOM_gdb.zip
  format: Geodatabase
  id: resource_c0fc1d47
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected cumulative water over Beledweyne City, Hiraan Region
    of Somalia between 12 and 25 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3599/FL20230327SOM_SHP.zip
  format: null
  id: resource_880a4166
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedcumulativewaterov_20230525
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-25'
temporal_resolution: null
title: Satellite detected cumulative water over Beledweyne City, Hiraan Region of
  Somalia between 12 and 25 May 2023
version: null
vulnerability: null
---
