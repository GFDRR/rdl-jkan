---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-district-hiraan-region-somalia-2791
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-district-hiraan-region-somalia-2791
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-district-hiraan-region-somalia-2791
dataset_id: rdls_hel-som_unosat_detectedwateroverbeletwey_20180507
description: 'This map illustrates satellite-detected flood water extent over the
  district of Belet Weyne, Hiraan region, Somalia using a SAR image from 06 May 2018
  and an optical VHR image over Beledweyne town. More than 2800 km2 of lands were
  assessed and about 19,000 ha (190km2) appear to be inundated which corresponds to
  about to about 7% of the total analysed zone. In this analysed area and according
  to WorldPop data the population is estimated to ~126,000 people, ~ 32,000 live in
  the flooded zone and about 70,000 within 100 meters distance from the flooded areas.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-district-hiraan-region-somalia-2791]'
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
    description: Population exposed to flood inundation and proximity zones in Belet
      Weyne District
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
license: CC-BY-SA-4.0
lineage:
  description: "Satellite imagery from SAR (06 May 2018) and optical VHR sensors were\
    \ analyzed by UNOSAT to detect flood water extent through multi-temporal image\
    \ comparison. Inundated area (190 km\xC2\xB2) was delineated and intersected with\
    \ WorldPop gridded population data to estimate affected populations in the flooded\
    \ zone and within 100m buffer zones."
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-district-hiraan-region-somalia-2791
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood inundation in Belet Weyne District
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
  description: Satellite detected water over Belet Weyne District,Hiraan Region, Somalia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20180501SOM/FL20180501SOM_SHP.zip
  format: null
  id: resource_4fb2f298
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180501SOM_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-som_unosat_detectedwateroverbeletwey_20180507
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
  start: '2018-05-07'
temporal_resolution: null
title: Satellite detected water over Belet Weyne District,Hiraan Region, Somalia
version: null
vulnerability: null
---
