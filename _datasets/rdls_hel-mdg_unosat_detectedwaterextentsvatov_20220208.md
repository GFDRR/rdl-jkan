---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-in-vatovavy-fitovinany-region-madagascar-as-of-8-february-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-in-vatovavy-fitovinany-region-madagascar-as-of-8-february-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-vatovavy-fitovinany-region-madagascar-as-of-8-february-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-vatovavy-fitovinany-region-madagascar-as-of-8-february-2022
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentsvatov_20220208
description: 'UNOSAT code: TC20220201MDG This map illustrates satellite-detected surface
  waters in Vatovavy Fitovinany region, Madagascar as of 8 February 2022 at 05:20
  local time. The flood analysis were carried out by using an automated analysis with
  Artificial Intelligence based methods. Within the analyzed area of about 3,800 km2,
  210 km2 of lands appear to be flooded. Based on Worldpop population data and the
  detected surface waters in the analyzed area, the potentially exposed population
  is 57,200 people mainly located in district of Vohipeno with ~ 30,000 people, and
  Manakara Atsimo with ~ 27,000 people, This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT. Important
  note: Flood analysis from radar images may underestimate the presence of standing
  waters in built-up areas and densely vegetated areas due to backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-vatovavy-fitovinany-region-madagascar-as-of-8-february-2022]'
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
    description: Potentially exposed population derived from WorldPop data intersected
      with detected flood extents
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
  description: "Satellite imagery acquired on 8 February 2022 was processed using\
    \ UNOSAT's AI-based automated analysis methods to detect surface water extents\
    \ across 3,800 km\xB2 in Vatovavy Fitovinany region. Detected flood areas (210\
    \ km\xB2) were intersected with WorldPop gridded population data to estimate potentially\
    \ exposed population. The dataset represents post-event observed flood mapping\
    \ from a cyclone event."
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
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-vatovavy-fitovinany-region-madagascar-as-of-8-february-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to detected flood waters in Vatovavy
      Fitovinany region
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
  description: Satellite detected water extents in Vatovavy Fitovinany region, Madagascar
    as of 8 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_gdb.zip
  format: Geodatabase
  id: resource_526acfb7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220201MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Vatovavy Fitovinany region, Madagascar
    as of 8 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220201MDG/TC20220201MDG_SHP.zip
  format: null
  id: resource_70c83873
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220201MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_detectedwaterextentsvatov_20220208
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
  start: '2022-02-08'
temporal_resolution: null
title: Satellite detected water extents in Vatovavy Fitovinany region, Madagascar
  as of 8 February 2022
version: null
vulnerability: null
---
