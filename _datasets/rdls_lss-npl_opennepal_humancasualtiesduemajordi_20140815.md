---
attributions:
- entity:
    affiliation: null
    email: null
    name: Environmental Statistics, 2013
    url: https://data.humdata.org/dataset/human-casualties-due-to-major-disasters-in-nepal-1983-2013
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/human-casualties-due-to-major-disasters-in-nepal-1983-2013
creator:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/human-casualties-due-to-major-disasters-in-nepal-1983-2013
dataset_id: rdls_lss-npl_opennepal_humancasualtiesduemajordi_20140815
description: 'This dataset contains human casualties due to major disater such as
  flood and landslides, Earthquake, Windstorms, halitstrosm and thuderbolt, Avalanche,
  Fire, Cold wave, Drowning and Stampede for 1983 to 2013. The data sets is extracted
  from Environmental Statistics, 2013. (http://cbs.gov.np/wp-content/uploads/2014/07/Environment%20Statistics%20...).
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/human-casualties-due-to-major-disasters-in-nepal-1983-2013]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: Human casualty data extracted from Nepal's Environmental Statistics
    2013 publication, compiled by the Central Bureau of Statistics from official disaster
    records covering major hazard events (floods, landslides, earthquakes, windstorms,
    hailstorms, thunderbolts, avalanches, fires, cold waves, drowning, and stampedes)
    across Nepal from 1983 to 2013.
  sources:
  - id: source_1
    license: null
    name: Environmental Statistics, 2013
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/human-casualties-due-to-major-disasters-in-nepal-1983-2013
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Human casualties from flood events in Nepal, 1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Human casualties from landslide events in Nepal, 1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Human casualties from earthquake events in Nepal, 1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Human casualties from windstorm events in Nepal, 1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Human casualties from hailstorm and thunderbolt events in Nepal,
      1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Human casualties from avalanche events in Nepal, 1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Human casualties from fire events in Nepal, 1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_7
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Human casualties from cold wave events in Nepal, 1983-2013
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
    id: loss_8
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
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
  description: Nepal - Human Casualties due to Major Disasters in Nepal, 1983-2013
    (human%20casualties.csv)
  download_url: http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/human%20casualties.csv&nid=4320
  format: null
  id: resource_dd876cc2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: human%20casualties.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_opennepal_humancasualtiesduemajordi_20140815
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-08-15'
temporal_resolution: null
title: Nepal - Human Casualties due to Major Disasters in Nepal, 1983-2013
version: null
vulnerability: null
---
