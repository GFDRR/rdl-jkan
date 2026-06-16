---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA Visible Infrared Imaging Radiometer Suite (VIIRS)
    url: https://data.humdata.org/dataset/fao-eve-global-flood-monitoring-system
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Space Agency WorldCover 10m 2021
    url: https://data.humdata.org/dataset/fao-eve-global-flood-monitoring-system
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Food and Agriculture Organization (FAO) of the United Nations
  url: https://data.humdata.org/dataset/fao-eve-global-flood-monitoring-system
creator:
  affiliation: null
  email: null
  name: Food and Agriculture Organization (FAO) of the United Nations
  url: https://data.humdata.org/dataset/fao-eve-global-flood-monitoring-system
dataset_id: rdls_hel-fao_eveglobalfloodmonitorings_2024
description: 'The DIEM Events Visualization in Emergencies (EVE) system provides resources
  to enhance the understanding of flood events and their impact on different land
  cover types, with a particular focus on agricultural areas. EVE provides a flood
  persistence analysis as well as an estimation of the population exposed to such
  events. EVE utilizes satellite-derived data from the NOAA Visible Infrared Imaging
  Radiometer Suite (VIIRS) at a 375-meter resolution, alongside land cover data from
  the European Space Agency''s WorldCover 10m 2021 dataset. Covering approximately
  40 countries, the system offers daily and biweekly insights, providing a continuously
  updated view of flood dynamics and their effects. Access the FAO EVE user guide
  to learn more. The platform presents results through interactive maps, charts, and
  tables, supporting decision-making in disaster management, agricultural planning,
  and environmental monitoring. Most resources are publicly accessible, though downloading
  aggregated data at the admin2 level requires a DIEM account . EVE products are preliminary
  analyses and have not yet undergone field validation. Users are encouraged to provide
  ground feedback to the FAO Data in Emergencies (DIEM) team to enhance the accuracy
  and utility of the data.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fao-eve-global-flood-monitoring-system]'
details: EVE analyses are based on global datasets to ensure broad coverage, rapid
  scalability, and integration into international humanitarian workflows. However,
  these datasets cannot always capture national or local specificities that would
  enhance analytical precision. While EVE can estimate the extent of flooded cropland,
  it does not determine whether the affected cropland was actively cultivated at the
  time of the flood. EVE does not inherently differentiate between hazardous and non-hazardous
  floods, which can lead to false detections in agricultural regions. Some flood events
  result from regular seasonal patterns or controlled agricultural activities, such
  as rice paddy planting or aquaculture, rather than actual hazard-related floods.
exposure:
- asset_type:
    description: Cropland area exposed to flood inundation derived from ESA WorldCover
      10m 2021 dataset
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Population exposed to flood events at administrative unit level
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
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
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAO EVE system processes NOAA VIIRS satellite imagery at 375m resolution
    to detect active flood extent and persistence, intersects results with ESA WorldCover
    10m land cover data to quantify cropland exposure, and overlays administrative
    boundaries to estimate population exposure across ~40 countries, generating event-based
    flood impact records at sub-national administrative levels.
  sources:
  - id: source_1
    license: null
    name: NOAA Visible Infrared Imaging Radiometer Suite (VIIRS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: European Space Agency WorldCover 10m 2021
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fao-eve-global-flood-monitoring-system
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Cropland area flooded during observed flood events
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
          quantity_kind: area
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposed to observed flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: '[EVE user guide]((see referenced_by))'
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data-in-emergencies.fao.org/documents/3335ee769a4e45708e27d2ee25d13bef/about
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for all countries from 1 July 2024 (when available)
    to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/6bdc6dcd-355d-43d8-afcd-c96ef40ee290/download/global-flood-events-fao-eve.csv
  format: null
  id: resource_6bdc6dcd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: global-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Afghanistan from 1 July 2024 (when available) to
    date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/867cc8f0-64a0-4a8c-90a8-ce1f5ac95ae4/download/afg-flood-events-fao-eve.csv
  format: null
  id: resource_867cc8f0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Angola from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/635ffafa-f5fb-4da3-8c64-a9a1d8b4afc9/download/ago-flood-events-fao-eve.csv
  format: null
  id: resource_635ffafa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ago-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Bangladesh from 1 July 2024 (when available) to
    date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/f92dd907-42aa-4cd2-9363-435776d89f97/download/bgd-flood-events-fao-eve.csv
  format: null
  id: resource_f92dd907
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Burkina Faso from 1 July 2024 (when available)
    to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/8b653f0a-d735-4654-9a9c-99445a8686ba/download/bfa-flood-events-fao-eve.csv
  format: null
  id: resource_8b653f0a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Burundi from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/cc6d4f72-22e2-426f-bc83-04799fbf3ead/download/bdi-flood-events-fao-eve.csv
  format: null
  id: resource_cc6d4f72
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bdi-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Cambodia from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/dd828c94-a4df-4c49-b179-8a0600027646/download/khm-flood-events-fao-eve.csv
  format: null
  id: resource_dd828c94
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: khm-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Cameroon from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/f2b255ed-b6b3-4ae7-be46-34d3f7f73012/download/cmr-flood-events-fao-eve.csv
  format: null
  id: resource_f2b255ed
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cmr-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Central African Republic from 1 July 2024 (when
    available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/4f48991d-e31f-4d83-b269-9840085b0de7/download/caf-flood-events-fao-eve.csv
  format: null
  id: resource_4f48991d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Chad from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/d6939365-59bc-40e1-b927-a5ad14d569d3/download/tcd-flood-events-fao-eve.csv
  format: null
  id: resource_d6939365
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Colombia from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/6043a417-557f-4e46-8a00-270c28ea16a2/download/col-flood-events-fao-eve.csv
  format: null
  id: resource_6043a417
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Democratic Republic of the Congo from 1 July 2024
    (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/b70cc1c9-d6f3-45e3-9117-50579ed38e43/download/cod-flood-events-fao-eve.csv
  format: null
  id: resource_b70cc1c9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Haiti from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/58fa6b4c-14d0-4c85-a8fc-a2273bf41813/download/hti-flood-events-fao-eve.csv
  format: null
  id: resource_58fa6b4c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Honduras from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/332a972a-33cd-4aa8-890f-3b1a82ea6f5b/download/hnd-flood-events-fao-eve.csv
  format: null
  id: resource_332a972a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hnd-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Iraq from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/f9ba364f-6277-4e88-945a-43fdd72658db/download/irq-flood-events-fao-eve.csv
  format: null
  id: resource_f9ba364f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Lao People's Democratic Republic from 1 July 2024
    (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/d473caee-d1ff-4a21-8d24-18adfa1e4201/download/lao-flood-events-fao-eve.csv
  format: null
  id: resource_d473caee
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Madagascar from 1 July 2024 (when available) to
    date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/4b73856c-9a04-46ba-9f30-5dd2979a7705/download/mdg-flood-events-fao-eve.csv
  format: null
  id: resource_4b73856c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mdg-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Malawi from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/0af0a0af-a4b5-46e9-8414-2c21e3b4c00f/download/mwi-flood-events-fao-eve.csv
  format: null
  id: resource_0af0a0af
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Mali from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/6fec05a1-6457-4233-8df9-ee36fb62a4c9/download/mli-flood-events-fao-eve.csv
  format: null
  id: resource_6fec05a1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mli-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Mozambique from 1 July 2024 (when available) to
    date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/e1e69686-3dfa-4a9d-84f5-4caced773d44/download/moz-flood-events-fao-eve.csv
  format: null
  id: resource_e1e69686
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Myanmar from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/133046d7-05ae-42f0-9649-741c1b288feb/download/mmr-flood-events-fao-eve.csv
  format: null
  id: resource_133046d7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mmr-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Namibia from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/3e70e14d-d95c-4578-9c5e-ca439318494d/download/nam-flood-events-fao-eve.csv
  format: null
  id: resource_3e70e14d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Nepal from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/89dec06d-cab1-463f-8c6f-057edb0c8783/download/npl-flood-events-fao-eve.csv
  format: null
  id: resource_89dec06d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Niger from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/3d8ee86c-8b42-45ae-860a-e4f7dc74648d/download/ner-flood-events-fao-eve.csv
  format: null
  id: resource_3d8ee86c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ner-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Nigeria from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/b998cd70-b5be-49dc-8954-77be0ae7719d/download/nga-flood-events-fao-eve.csv
  format: null
  id: resource_b998cd70
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Pakistan from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/d9b80ae9-867c-4f44-8aca-65a115a0fcd9/download/pak-flood-events-fao-eve.csv
  format: null
  id: resource_d9b80ae9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pak-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Philippines from 1 July 2024 (when available) to
    date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/834230fc-d1ee-4bfe-93a7-3da0e9453384/download/phl-flood-events-fao-eve.csv
  format: null
  id: resource_834230fc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Somalia from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/017dd932-4733-4da4-b598-1e1e2b4ecbec/download/som-flood-events-fao-eve.csv
  format: null
  id: resource_017dd932
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for South Sudan from 1 July 2024 (when available) to
    date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/82ca2db7-440f-4bad-bb0e-490823239591/download/ssd-flood-events-fao-eve.csv
  format: null
  id: resource_82ca2db7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ssd-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Sri Lanka from 1 July 2024 (when available) to
    date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/8df139ba-e6c9-4036-a090-52458829c931/download/lka-flood-events-fao-eve.csv
  format: null
  id: resource_8df139ba
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lka-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Sudan from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/58206a26-2124-4f3b-9828-b008f6d6dfdc/download/sdn-flood-events-fao-eve.csv
  format: null
  id: resource_58206a26
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sdn-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Thailand from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/88cb692f-e13c-4148-904c-f2e871ee4cb3/download/tha-flood-events-fao-eve.csv
  format: null
  id: resource_88cb692f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tha-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for United Republic of Tanzania from 1 July 2024 (when
    available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/26c6aeb2-e127-4b2a-ab42-9b4d22da8e24/download/tza-flood-events-fao-eve.csv
  format: null
  id: resource_26c6aeb2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Viet Nam from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/22dad400-9c2e-4ce9-9e5a-4f6b66ed20d4/download/vnm-flood-events-fao-eve.csv
  format: null
  id: resource_22dad400
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vnm-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Yemen from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/5b404124-4269-4475-a946-273a4580d64c/download/yem-flood-events-fao-eve.csv
  format: null
  id: resource_5b404124
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yem-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Zambia from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/3add3c40-37f2-4f37-ad27-f91deb4626da/download/zmb-flood-events-fao-eve.csv
  format: null
  id: resource_3add3c40
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Zimbabwe from 1 July 2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/e16d000a-308b-433c-a583-4a45d1470eed/download/zwe-flood-events-fao-eve.csv
  format: null
  id: resource_e16d000a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zwe-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Democratic People's Republic of Korea from 1 July
    2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/505c41a6-815a-4322-8f2e-32486b0d6f06/download/prk-flood-events-fao-eve.csv
  format: null
  id: resource_505c41a6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk-flood-events-fao-eve.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Biweekly insights on flood events - their impacts on population and
    various land cover types - for Venezuela (Bolivarian Republic of) from 1 July
    2024 (when available) to date.
  download_url: https://data.humdata.org/dataset/1fa3b0d1-4b0b-415b-a978-8b4dbf50d1ca/resource/bc581b6c-328e-4679-a03b-2fa31bd83eb7/download/ven-flood-events-fao-eve.csv
  format: null
  id: resource_bc581b6c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven-flood-events-fao-eve.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-fao_eveglobalfloodmonitorings_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - IRQ
  - VNM
  - YEM
  - AFG
  - AGO
  - BGD
  - BFA
  - BDI
  - KHM
  - CMR
  - CAF
  - TCD
  - COL
  - HTI
  - HND
  - LAO
  - MDG
  - MWI
  - MLI
  - MOZ
  - NER
  - NGA
  - PAK
  - PNG
  - PHL
  - RWA
  - SEN
  - SLE
  - SOM
  - SSD
  - SDN
  - SYR
  - TZA
  - TGO
  - UGA
  - ZMB
  - ZWE
  - ETH
  - KEN
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2024-01-07'
temporal_resolution: null
title: FAO EVE Global Flood Monitoring System
version: null
vulnerability: null
---
