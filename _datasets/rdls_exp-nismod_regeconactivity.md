---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ivann Schlosser
    url: https://orcid.org/0009-0004-4099-3198
  id: attribution_creator2
  role: creator
- entity:
    affiliation: null
    email: fcdo.correspondence@fcdo.gov.uk
    name: UK Foreign, Commonwealth and Development Office (FCDO)
    url: https://www.gov.uk/government/organisations/foreign-commonwealth-development-office
  id: attribution_funder
  role: funder
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Tom Russell
  url: https://orcid.org/0000-0002-0081-400X
creator:
  affiliation: null
  email: null
  name: Tom Russell
  url: https://orcid.org/0000-0002-0081-400X
dataset_id: rdls_exp-nismod_regeconactivity
description: 'A curated collection of open geospatial datasets processed to support
  downscaling of regional economic activity from national/subnational levels to high-resolution
  grids globally. The collection includes agricultural GDP by subsector (crop, livestock,
  forestry, fisheries), gridded GDP data, built environment indicators, points of
  interest from Overture Maps and Foursquare, population and settlement layers, land
  cover classifications, power generation facilities, and mining locations. All datasets
  are harmonized to cloud-optimized Parquet format and H3 hexagonal grid system to
  enable analysis of economic activity distribution across three dimensions: Location
  (high spatial resolution), Category (economic sectors following ISIC classification),
  and Output (GDP/GVA quantification). This package provides standardized inputs for
  developing Bayesian Hierarchical Models that infer 20-sector gridded regional Gross
  Value Added (rGVA) globally by incorporating multi-scale, multi-sector priors.'
details: 'This is version 0.1.0 of a curated data package developed for the validation
  workshop - Downscaling of global economic activity data - held at Oxford University
  on 15 May 2025. All datasets have been transformed from their original sources into
  cloud-optimized Parquet format and spatially harmonized using H3 hexagonal grid
  (resolutions 7-10, approximately 5km-100m cell sizes) via the scalenav framework
  built on DuckDB and Ibis for large-scale spatial analysis. The processing methodology
  implements pycnophylactic spatial downscaling (mass-preserving interpolation) and
  maps Points of Interest to ISIC codes for sector-specific economic disaggregation.
  Datasets are accessible via cloud object storage (S3: s3://gri-datapkg/spatial-economics/v0.1.0/)
  without download requirements. All data sources are attributed to original creators
  and carry their respective licenses; processing code is available under MIT license
  on GitHub. Spatial coverage is global with example applications in UK, Thailand,
  and Ghana; temporal coverage spans primarily 2010-2024 with some historical data
  to 1990. The final model outputs (20-sector gridded rGVA globally) are work-in-progress
  and will be released separately; this package contains input and validation datasets
  used in model development.'
exposure:
- asset_type:
    description: Gridded GDP data classified using the GEM GED4ALL schema, derived
      from aggregate GDP statistics (DOSE-WDI) and agricultural production data (MapSPAM)
      disaggregated to a spatial grid.
    id: gridded_gdp
    scheme: GED4ALL
    title: Economic indicator taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: economic_indicator
  id: exposure_gridded_gdp
  metrics:
  - dimension: product
    id: metric_agricultural_gdp
    measurement:
      quantity_kind: monetary
      unit: USD
  - dimension: product
    id: metric_gridded_gdp
    measurement:
      quantity_kind: monetary
      unit: USD
- asset_type:
    description: Population exposure data classified using the GEM GED4ALL schema,
      sourced from GHS-POP (Global Human Settlement Population Grid).
    id: population
    scheme: GED4ALL
    title: Population taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: population
  id: exposure_demographic
  metrics:
  - dimension: population
    id: metric_population
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Built-up surface area classified using the GEM GED4ALL schema, sourced
      from GHS-BUILT-S (Global Human Settlement Built-up Surface Grid).
    id: built_up_surface_area
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_builtup
  metrics:
  - dimension: structure
    id: metric_built_area
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Points of interest classified using the GEM GED4ALL schema, sourced
      from Overture Maps Foundation open data.
    id: points_of_interest
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_poi
  metrics:
  - dimension: structure
    id: metric_poi_count
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Power generation facilities classified using the GEM GED4ALL schema,
      sourced from the GEM Global Power Plant Database.
    id: power_generation_facilities
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_power_generation
  metrics:
  - dimension: structure
    id: metric_power_facilities
    measurement:
      quantity_kind: count
      unit: count
  - dimension: product
    id: metric_generation_capacity
    measurement:
      quantity_kind: power
      unit: null
- asset_type:
    description: Mining sites classified using the GEM GED4ALL schema, sourced from
      open global mining datasets.
    id: mining_sites
    scheme: null
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_mining
  metrics:
  - dimension: structure
    id: metric_mining_sites
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Land cover data classified using the GEM GED4ALL schema, sourced
      from Copernicus Global Land Service land cover products.
    id: land_cover
    scheme: null
    title: Land cover taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: natural_environment
  id: exposure_land_cover
  metrics:
  - dimension: content
    id: metric_land_cover
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: Multi-layer regional economic activity dataset assembled from global
    gridded and vector sources. Agricultural GDP from AgGDP and MAPSPAM crop production
    statistics; mining site boundaries from the Global-scale Mining Areas Dataset;
    power infrastructure from the GEM Global Integrated Power Tracker; gridded GDP
    from the Kummu et al. dataset; land cover from Copernicus Global Dynamic Land
    Cover; population and settlement from GHSL; points of interest from Overture Maps;
    economic development indicators from DOSE-WDI. Spatial aggregation and normalisation
    performed using scalenav.
  sources:
  - id: source_aggdp
    license: CC-BY-4.0
    name: AgGDP - Global Gridded Agricultural GDP
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.5194/essd-15-1357-2023
    used_in: exposure
  - id: source_mapspam
    license: CC-BY-4.0
    name: MAPSPAM - Global Spatially-Disaggregated Crop Production Statistics
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.7910/DVN/SWPENT
    used_in: exposure
  - id: source_mining
    license: CC-BY-SA-4.0
    name: Global-scale Mining Areas Dataset
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.1038/s41597-020-00624-w
    used_in: exposure
  - id: source_gem
    license: CC-BY-4.0
    name: GEM Global Integrated Power Tracker
    risk_data_type: null
    type: dataset
    url: https://globalenergymonitor.org/projects/global-integrated-power-tracker/
    used_in: exposure
  - id: source_kummu_gdp
    license: CC-BY-4.0
    name: Kummu Gridded Global GDP Dataset
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.1038/s41597-025-04487-x
    used_in: exposure
  - id: source_copernicus
    license: CC-BY-4.0
    name: Copernicus Global Dynamic Land Cover
    risk_data_type: null
    type: dataset
    url: https://land.copernicus.eu/en/products/global-dynamic-land-cover
    used_in: exposure
  - id: source_ghsl
    license: CC-BY-4.0
    name: GHSL - Global Human Settlement Layer
    risk_data_type: null
    type: dataset
    url: https://ghsl.jrc.ec.europa.eu/
    used_in: exposure
  - id: source_overture
    license: ODbL-1.0
    name: Overture Maps Places
    risk_data_type: null
    type: dataset
    url: https://overturemaps.org/
    used_in: exposure
  - id: source_dose_wdi
    license: CC-BY-4.0
    name: DOSE-WDI
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.5281/zenodo.17235586
    used_in: exposure
  - id: source_scalenav
    license: MIT
    name: scalenav
    risk_data_type: null
    type: model
    url: https://github.com/nismod/scale-nav
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Climate Compatible Growth (CCG)
  url: https://climatecompatiblegrowth.com/
publisher:
  affiliation: null
  email: info@zenodo.org
  name: Zenodo
  url: https://zenodo.org
purpose: Provides standardized, analysis-ready geospatial datasets to support research
  on spatial economic modeling, infrastructure-economy interactions, and climate risk
  assessment. Addresses the critical gap in understanding how economic activity distributes
  spatially by enabling researchers to downscale coarse national/regional economic
  statistics to high-resolution grids while maintaining sectoral detail. Facilitates
  data-driven analysis of economic exposure in infrastructure climate risk assessments,
  regional economic planning, and sustainable development research. The processed
  datasets eliminate barriers to access by providing harmonized formats optimized
  for large-scale spatial analysis and machine learning applications in economic geography.
referenced_by: []
resources:
- access_url: https://doi.org/10.5281/zenodo.17235586
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'JSON file mapping dataset identifiers to their S3 cloud storage paths
    for direct access. Contains 18 entries pointing to processed Parquet datasets
    including: agricultural GDP subsectors (crop, fish, forest, livestock, total),
    Copernicus built-up area, DOSE-WDI economic output, GEM power tracker, JRC population
    and settlement layers (aggregated, building height, population, settlement area
    for 2018 and non-residential), Kummu GDP PPP, MAPSPAM crop yields, mining locations,
    and Overture places with land use (both filled and original versions). All datasets
    stored in cloud-optimized Parquet format at s3://gri-datapkg/spatial-economics/v0.1.0/
    with subdirectories by source and processing status.'
  download_url: https://zenodo.org/records/17235586/files/catalogue.json
  format: null
  id: resource_catalogue_json
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Dataset Catalogue
- access_url: https://doi.org/10.5281/zenodo.17235586
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CSV file providing structured metadata for all datasets in the collection
    including dataset names, descriptions, source attributions, licenses, temporal
    coverage, spatial coverage, and access methods. Lists 18 processed datasets with
    details on agricultural GDP (AgGDP subsectors), demographic data (GHSL population
    and built-up layers), land cover (Copernicus), economic indicators (DOSE-WDI,
    Kummu GDP), infrastructure (GEM power facilities, mining areas), points of interest
    (Overture Maps places and land use), and crop production statistics (MAPSPAM yields).
    Serves as human-readable documentation of the data collection contents and provenance.
  download_url: https://zenodo.org/records/17235586/files/global-spatial-economics-datasets-public.csv
  format: null
  id: resource_metadata_csv
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Dataset Metadata
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nismod_regeconactivity
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Data to Support Downscaling of Global Regional Economic Activity
version: 0.1.0
vulnerability: null
---
