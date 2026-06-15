---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
dataset_id: rdls_hzd-coclico_floodmaps
description: 'Dataset indicating flood extents as a result of climate change projections
  (0-4 m SLR, per 0.5 m). By relating very high-resolution topography maps to projected
  SLR, areas prone to marine submergence are identified. Coastal defenses (natural
  and man-made) are ought transparent for the calculations. This dataset is hosted
  through WMS servers from BRGM (https://sealevelrise.brgm.fr/slr). See this article
  (https://doi.org/10.1007/978-3-319-74669-2_12) for more dataset-specific information.
  Variants in the source dataset - slr: 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, ...
  (1 more). [Source: This metadata record was automatically extracted from the STAC
  catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: 'Sea-level rise scenario sweep (source: Collection.summaries.slr).'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_flood
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: event_slr_scenarios
        occurrence:
          deterministic:
            description: null
            index_criteria: Sea-level rise scenarios (metres)
            thresholds:
            - 0.0 m
            - 0.5 m
            - 1.0 m
            - 1.5 m
            - 2.0 m
            - 2.5 m
            - 3.0 m
            - 3.5 m
            - 4.0 m
          empirical: null
          probabilistic: null
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://example.org/license/unknown
lineage:
  description: Dataset indicating flood extents as a result of climate change projections
    (0-4 m SLR, per 0.5 m). By relating very high-resolution topography maps to projected
    SLR, areas prone to marine submergence are identified. Coastal defenses (natural
    and man-made) are ought transparent for the calculations. This dataset is hosted
    through WMS servers from BRGM (https://sealevelrise.brgm.fr/slr). See this article
    (https://doi.org/10.1007/978-3-319-74669-2_12) for more dataset-specific information.
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - hazard
    type: dataset
    url: https://www.deltares.nl
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/floodmaps/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Floodmaps [floodmaps]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/floodmaps.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Floodmaps
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-coclico_floodmaps
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015'
temporal_resolution: null
title: CoCliCo - Floodmaps
version: null
vulnerability: null
---
