---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/water-extents-in-iakora-and-ivohibe-districts-ihorombe-region-madagascar-as-of-24-february
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-in-iakora-and-ivohibe-districts-ihorombe-region-madagascar-as-of-24-february
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-iakora-and-ivohibe-districts-ihorombe-region-madagascar-as-of-24-february
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-iakora-and-ivohibe-districts-ihorombe-region-madagascar-as-of-24-february
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentsiakor_20220302
description: 'UNOSAT code: TC20220221MDG This map illustrates satellite-detected surface
  waters in Iakora and Ivohibe Districts, Ihorombe Region, Madagascar as observed
  from a Sentinel-2 image acquired on 24 February 2022 at 10:00 local time. Within
  the analyzed cloud free zones of about 150 km2, a total of about 28 km2 of lands
  appear to be flooded. Based on Worldpop population data and the detected surface
  waters, about 1,200 people are potentially exposed or living close to flooded areas.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-iakora-and-ivohibe-districts-ihorombe-region-madagascar-as-of-24-february]'
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 24 February 2022 to detect surface water extents through visual comparison and\
    \ change detection methods. Detected flooded areas (~28 km\xC2\xB2) were intersected\
    \ with WorldPop population data to estimate approximately 1,200 people potentially\
    \ exposed to flooding in Iakora and Ivohibe Districts."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2
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
- href: https://data.humdata.org/dataset/water-extents-in-iakora-and-ivohibe-districts-ihorombe-region-madagascar-as-of-24-february
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by detected surface water flooding
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
  description: Satellite detected water extents in Iakora and Ivohibe Districts, Ihorombe
    Region, Madagascar as of 24 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_gdb.zip
  format: Geodatabase
  id: resource_651748b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Iakora and Ivohibe Districts, Ihorombe
    Region, Madagascar as of 24 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_SHP.zip
  format: null
  id: resource_f54ab4af
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_detectedwaterextentsiakor_20220302
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
  start: '2022-03-02'
temporal_resolution: null
title: Satellite detected water extents in Iakora and Ivohibe Districts, Ihorombe
  Region, Madagascar as of 24 February 2022
version: null
vulnerability: null
---
