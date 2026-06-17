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
dataset_id: rdls_hzd-coclico_sc
description: 'Projections of global shoreline change in view of climate change. This
  assessment considers the combined effects of ambient change (historical trends),
  sea level rise (RCP4.5 and RCP8.5) and storm driven (instantaneous) erosion. Data
  is computed for seven ensembles (1, 5, 17, 50, 83, 95 and 99th percentile) and two
  timesteps (2050 and 2100). This dataset is part of the LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST)
  project. See this article (https://doi.org/10.1038/s41558-020-0697-0) for more dataset-specific
  information. Variants in the source dataset - ensemble: 1, 5, 17, 50, 83, 95, 99;
  scenarios: RCP45, RCP85; time: 2050-01-01T00:00:00Z, 2100-01-01T00:00:00Z - time;
  lon: -179.3, 179.43 - longitude; lat: -55.973, 66.414 - latitude. [Source: This
  metadata record was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: Er:m/yr
      process: coastal_erosion
      trigger: null
      type: erosion
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: erosion
license: https://example.org/license/unknown
lineage:
  description: Projections of global shoreline change in view of climate change. This
    assessment considers the combined effects of ambient change (historical trends),
    sea level rise (RCP4.5 and RCP8.5) and storm driven (instantaneous) erosion. Data
    is computed for seven ensembles (1, 5, 17, 50, 83, 95 and 99th percentile) and
    two timesteps (2050 and 2100). This dataset is part of the LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST)
    project. See this article (https://doi.org/10.1038/s41558-020-0697-0) for more
    dataset-specific information.
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
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/sc/collection.json
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
  title: 'STAC Collection: CoCliCo - Shoreline change [sc]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The root of the Global shoreline change projections for the year 2050
    under RCP4.5 zarr dataset on public Google Cloud Storage.
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/shoreline_change_projections.zarr
  format: null
  id: resource_data
  media_type: application/vnd.zarr
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global shoreline change projections for the year 2050 under RCP4.5 zarr root
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/sc.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Shoreline change
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
slug: rdls_hzd-coclico_sc
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
temporal: null
temporal_resolution: null
title: CoCliCo - Shoreline change
version: null
vulnerability: null
---
