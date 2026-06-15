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
dataset_id: rdls_hzd-coclico_smd
description: 'Global long-term (1984-2015) shoreline evolution based on satellite
  observations. Per transect location (500 m spaced) it is assessed what the change
  from land to sea, land to active zone and active zone to sea (erosion) as well as
  sea to land, sea to active zone and active zone to land (accretion) is. This dataset
  is part of the LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST) project.
  See this article (https://doi.org/10.1038/s41598-018-30904-w) for more dataset-specific
  information. Variants in the source dataset - lon: -179.999350134, 179.999547763
  - longitude; lat: -62.9936453412, 62.9965817763 - latitude. [Source: This metadata
  record was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    erosion:
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
  event_sets_count: 1
license: https://example.org/license/unknown
lineage:
  description: Global long-term (1984-2015) shoreline evolution based on satellite
    observations. Per transect location (500 m spaced) it is assessed what the change
    from land to sea, land to active zone and active zone to sea (erosion) as well
    as sea to land, sea to active zone and active zone to land (accretion) is. This
    dataset is part of the LISCOAST (https://data.jrc.ec.europa.eu/collection/LISCOAST)
    project. See this article (https://doi.org/10.1038/s41598-018-30904-w) for more
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
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/smd/collection.json
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
  title: 'STAC Collection: CoCliCo - Global shoreline morphodynamics [smd]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Global shoreline morphodynamics (The root of the smd zarr
    dataset on public Google Cloud Storage.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/global_shoreline_morphodynamics.zarr
  format: null
  id: resource_data
  media_type: application/vnd.zarr
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: smd zarr root
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/smd.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Global shoreline morphodynamics
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
slug: rdls_hzd-coclico_smd
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
title: CoCliCo - Global shoreline morphodynamics
version: null
vulnerability: null
---
