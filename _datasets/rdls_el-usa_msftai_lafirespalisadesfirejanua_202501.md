---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet Labs SkySat imagery
    url: https://data.humdata.org/dataset/palisades-fire-building-damage-assessment
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Maxar satellite imagery
    url: https://data.humdata.org/dataset/palisades-fire-building-damage-assessment
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Overture Maps
    url: https://data.humdata.org/dataset/palisades-fire-building-damage-assessment
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Microsoft AI for Good Lab damage assessment model
    url: https://data.humdata.org/dataset/palisades-fire-building-damage-assessment
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/palisades-fire-building-damage-assessment
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/palisades-fire-building-damage-assessment
dataset_id: rdls_el-usa_msftai_lafirespalisadesfirejanua_202501
description: 'We ran our damage assessment AI models on images provided by Planet
  and Maxar and have mapped out the affected buildings. The images cover Palisades
  fires. Analysis was done on: 1) Planet''s 20250108_222134_ssc10 SkySat scene captured
  01/08 2) Planet''s 20250109_221527_ssc10 SkySat scene captured 01/09 3) Maxar imagery
  1050010040277500 captured 1/10 Latest results show the following. Total of 18,538
  structures: 11,735 not damaged 6,803 damaged. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/palisades-fire-building-damage-assessment]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
exposure:
- asset_type:
    description: Building footprints from Overture Maps classified by damage status
      from AI assessment
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building footprints from Overture Maps were intersected with high-resolution
    satellite imagery from Planet Labs (SkySat) and Maxar captured during and immediately
    after the Palisades fire (01/08-01/10/2025). Microsoft's AI damage assessment
    model was applied to classify each structure as damaged or not damaged, resulting
    in a post-event damage inventory of 18,538 structures with 6,803 confirmed damaged.
  sources:
  - id: source_1
    license: null
    name: Planet Labs SkySat imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Maxar satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Overture Maps
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: Microsoft AI for Good Lab damage assessment model
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/palisades-fire-building-damage-assessment
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from Palisades wildfire using AI
      models on satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://overturemaps.org/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Results from 1/10 using Maxar imagery. Total of 18,538 structures
    in this AOI: 11,735 not damaged 6,803 damaged The result file contains the following
    fields for each building footprint: damage_pct_0m - the fraction of the building
    footprint''s area that is classified as damaged by our model damage_pct_10m -
    total damaged area within a 10m buffer of the building footprint (including the
    footprint itself) / building footprint''s area (this can be >1.0 but we clip to
    1.0) damage_pct_20m - same as above but with a 20m buffer damaged - 1 if damage_pct_0m
    > 0 else 0 unknown_pct - fraction of the pixels within the building footprint
    that we think are obstructed (clouds, smoke, haze, too dark to evaluate)'
  download_url: https://data.humdata.org/dataset/30768ff0-289b-4fda-96d9-7209243c984d/resource/9650c5fe-c29b-429e-81e3-537688a74f60/download/maxar_palisades_1050010040277500_damage_predictions.gpkg
  format: null
  id: resource_9650c5fe
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maxar_palisades_1050010040277500_damage_predictions.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States - LA Fires - Palisades fire January 2025: Building Damage
    Assessment (Mask from 01/09 using Planet imagery.)'
  download_url: https://data.humdata.org/dataset/30768ff0-289b-4fda-96d9-7209243c984d/resource/4f04b37a-8aa0-46bd-abe5-463d2dc5c453/download/20250109_221527_ssc7_u0001_data_mask.geojson
  format: null
  id: resource_4f04b37a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250109_221527_ssc7_u0001_data_mask.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Results from 01/09 using Planet imagery. 20,095 total structures in
    this AOI: 4,380 unknown 12,063 in 0-20 bucket 3,652 in damaged/destroyed bucket
    The result file contains the following fields for each building footprint: damage_pct_0m
    - the fraction of the building footprint''s area that is classified as damaged
    by our model damage_pct_10m - total damaged area within a 10m buffer of the building
    footprint (including the footprint itself) / building footprint''s area (this
    can be >1.0 but we clip to 1.0) damage_pct_20m - same as above but with a 20m
    buffer damaged - 1 if damage_pct_0m > 0 else 0 unknown_pct - fraction of the pixels
    within the building footprint that we think are obstructed (clouds, smoke, haze,
    too dark to evaluate)'
  download_url: https://data.humdata.org/dataset/30768ff0-289b-4fda-96d9-7209243c984d/resource/2fa2005b-a988-4701-9424-4355a3f146b7/download/20250109_221527_ssc7_u0001_damage_predictions.gpkg
  format: null
  id: resource_2fa2005b
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250109_221527_ssc7_u0001_damage_predictions.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Results from 01/08 using Planet imagery. There are 17,835 footprints
    in the imagery area. Of those: 6251 are covered by clouds, shadow, and/or smoke
    9229 are in the lowest 0-20% bucket 2355 are in the >20% bucket The result file
    contains the following fields for each building footprint: damage_pct_0m - the
    fraction of the building footprint''s area that is classified as damaged by our
    model damage_pct_10m - total damaged area within a 10m buffer of the building
    footprint (including the footprint itself) / building footprint''s area (this
    can be >1.0 but we clip to 1.0) damage_pct_20m - same as above but with a 20m
    buffer damaged - 1 if damage_pct_0m > 0 else 0 unknown_pct - fraction of the pixels
    within the building footprint that we think are obstructed (clouds, smoke, haze,
    too dark to evaluate)'
  download_url: https://data.humdata.org/dataset/30768ff0-289b-4fda-96d9-7209243c984d/resource/0bf4f7a6-6c95-4580-957e-7b73f4963614/download/20250108_222134_ssc10_u0001_damage_predictions.gpkg
  format: null
  id: resource_0bf4f7a6
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250108_222134_ssc10_u0001_damage_predictions.gpkg
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-usa_msftai_lafirespalisadesfirejanua_202501
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-01-10'
  start: '2025-01-08'
temporal_resolution: null
title: 'United States - LA Fires - Palisades fire January 2025: Building Damage Assessment'
version: null
vulnerability: null
---
