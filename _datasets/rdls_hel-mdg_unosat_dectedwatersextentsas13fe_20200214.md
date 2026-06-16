---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS-NOAA
    url: https://data.humdata.org/dataset/satellite-dected-waters-extents-as-of-13-february-2020-over-the-republic-of-madagascar
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-dected-waters-extents-as-of-13-february-2020-over-the-republic-of-madagascar
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-dected-waters-extents-as-of-13-february-2020-over-the-republic-of-madagascar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-dected-waters-extents-as-of-13-february-2020-over-the-republic-of-madagascar
dataset_id: rdls_hel-mdg_unosat_dectedwatersextentsas13fe_20200214
description: 'UNOSAT code: FL20200128MDG This maps illustrates satellite-detected
  water via VIIRS-NOAA on the center and the northern part of the Republic of Madagascar
  between the 09 and the 13 February 2020. Within the analysed extent not covered
  by clouds, a total of about 9,116 km2 appear to be flooded, of which about 2,098
  km2, 1,366 km2 and 834 km2 in Boeny, Melaky and Alaotra-Mangoro region respectively.
  Based on Worldpop population data and the detected surface waters, about 1,300,000
  people are potentially exposed or living close to flooded areas. In Boeny, Melaky
  and Alaotra-Mangoro regions, respectively 170,000; 35,000 and 80,000 people are
  potentially exposed or living close to flooded areas. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-dected-waters-extents-as-of-13-february-2020-over-the-republic-of-madagascar]'
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
    description: Population potentially exposed or living close to satellite-detected
      flooded areas based on WorldPop data
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
  description: "UNOSAT analysts processed VIIRS-NOAA satellite imagery acquired between\
    \ 9-13 February 2020 over Madagascar, detecting water extents through multi-temporal\
    \ image comparison and change analysis. Detected flooded areas (9,116 km\xC2\xB2\
    ) were intersected with WorldPop population data to estimate approximately 1.3\
    \ million people potentially exposed to flooding in affected regions."
  sources:
  - id: source_1
    license: null
    name: VIIRS-NOAA
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
- href: https://data.humdata.org/dataset/satellite-dected-waters-extents-as-of-13-february-2020-over-the-republic-of-madagascar
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by satellite-detected flooding in Madagascar,
      February 2020
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Satellite dected waters extents, as of 13 February 2020 over the Republic
    of Madagascar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/FL20200128MDG/FL20200128MDG_gdb.zip
  format: Geodatabase
  id: resource_b71e4527
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200128MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite dected waters extents, as of 13 February 2020 over the Republic
    of Madagascar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/FL20200128MDG/FL20200128MDG_SHP.zip
  format: null
  id: resource_5ee7ec1d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200128MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_dectedwatersextentsas13fe_20200214
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-02-14'
temporal_resolution: null
title: Satellite dected waters extents, as of 13 February 2020 over the Republic of
  Madagascar
version: null
vulnerability: null
---
